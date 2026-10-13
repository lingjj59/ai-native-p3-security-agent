"""Fixed planner -> controller -> simulator -> evidence -> bounded report."""

import hashlib
import json
import platform
import subprocess
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

from .controller import Controller
from .executor import Simulator
from .registry import CHECKS, CONTRACT_VERSION, ORDER, POLICY_VERSION, REGISTRY_VERSION, TARGET_ID
from .reporting import classify


def write_json(path: Path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def run(fixture: dict, output_root: Path, *, target_id=TARGET_ID, proposals=ORDER,
        max_attempts=8, logical_budget=90) -> Path:
    controller = Controller(max_attempts=max_attempts, logical_budget=logical_budget)
    simulator = Simulator(fixture)
    run_id = "run-" + uuid.uuid4().hex
    destination = output_root / run_id
    destination.mkdir(parents=True, exist_ok=False)
    source_root = Path(__file__).resolve().parents[2]
    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=source_root, text=True).strip()
        dirty = bool(subprocess.check_output(["git", "status", "--porcelain"], cwd=source_root, text=True).strip())
    except (OSError, subprocess.CalledProcessError):
        commit, dirty = "unavailable", None
    fixture_hash = hashlib.sha256(json.dumps(fixture, sort_keys=True).encode()).hexdigest()
    metadata = {
        "run_id": run_id, "commit": commit, "working_tree_dirty_at_start": dirty,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "contract_version": CONTRACT_VERSION, "registry_version": REGISTRY_VERSION,
        "policy_version": POLICY_VERSION, "fixture_id": fixture["fixture_id"],
        "fixture_version": fixture["version"], "fixture_sha256": fixture_hash,
        "environment": {"python": platform.python_version(), "platform": platform.platform()},
        "target_id": target_id, "source": "fixture_demo", "evidence_level": "OBSERVED",
        "model_id": None, "prompt_version": None, "model_calls": 0, "tokens": 0,
        "model_cost": 0, "human_signoff": "pending",
        "budgets": {"max_attempts": controller.max_attempts, "max_rounds": controller.max_rounds,
                    "logical_seconds": controller.logical_budget, "concurrency": 1, "retries": 0},
    }
    write_json(destination / "metadata.json", metadata)
    write_json(destination / "fixture.json", fixture)
    results = {tid: {"test_id": tid, "execution_status": "NOT_RUN", "conclusion": "INCONCLUSIVE",
                     "reason": "not_scheduled", "evidence_ids": []} for tid in CHECKS}
    started = time.perf_counter()
    sequence = 0
    stop_reason = "plan_finished"
    with (destination / "events.jsonl").open("x", encoding="utf-8", newline="\n") as stream:
        def event(kind, **fields):
            nonlocal sequence
            sequence += 1
            evidence_id = f"{run_id}:E{sequence:03d}"
            stream.write(json.dumps({"run_id": run_id, "evidence_id": evidence_id,
                                     "sequence": sequence, "event": kind, **fields}, ensure_ascii=False) + "\n")
            stream.flush()  # A write failure raises and prevents the next action.
            return evidence_id

        for test_id in proposals:
            allowed, reason = controller.admit(target_id, test_id)
            decision_id = event("controller_decision", test_id=test_id, allowed=allowed, reason=reason)
            if not allowed:
                if test_id in results and results[test_id]["execution_status"] == "NOT_RUN":
                    results[test_id].update(execution_status="DENIED", reason=reason, evidence_ids=[decision_id])
                if "budget_exhausted" in reason:
                    stop_reason = reason
                    break
                continue
            event("execution_started", test_id=test_id, attempt_index=1,
                  actor_ref=CHECKS[test_id].actor, resource_ref=CHECKS[test_id].resource)
            observation = simulator.execute(test_id)
            evidence_id = event("observation", test_id=test_id, actual_result=observation)
            conclusion, reason = classify(test_id, observation)
            controller.observe(test_id, observation["logical_seconds"], conclusion == "NOT_CONFIRMED")
            results[test_id].update(execution_status="EXECUTED", conclusion=conclusion,
                                   reason=reason, evidence_ids=[evidence_id])
        event("run_stopped", reason=stop_reason, actual_attempts=controller.attempts)
    report = {**metadata, "results": list(results.values()), "stop_reason": stop_reason,
              "actual_attempts": controller.attempts, "planner_rounds": controller.rounds,
              "logical_seconds": controller.logical_time, "wall_seconds": time.perf_counter() - started,
              "uncovered": [tid for tid, value in results.items() if value["conclusion"] == "INCONCLUSIVE"],
              "limits": "Offline fixture only; no live target, model planner or independent peer verification."}
    write_json(destination / "report.json", report)
    files = ("metadata.json", "fixture.json", "events.jsonl", "report.json")
    write_json(destination / "checksums.json", {
        name: hashlib.sha256((destination / name).read_bytes()).hexdigest() for name in files
    })
    return destination
