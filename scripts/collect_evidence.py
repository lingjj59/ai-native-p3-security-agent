"""Collect reproducible submission evidence from a clean committed checkout."""

import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    status = subprocess.check_output(["git", "status", "--porcelain"], cwd=ROOT, text=True)
    if status.strip():
        raise SystemExit("Commit or preserve local changes before collecting submission evidence.")
    if (ROOT / "evidence" / "manifest.json").exists():
        raise SystemExit("Submission manifest already exists; preserve it and use individual demo runs.")
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    commands = {
        "tests.txt": ["-m", "unittest", "discover", "-s", "eval", "-v"],
        "compile.txt": ["-m", "compileall", "-q", "src", "scripts", "eval"],
        "docs.txt": ["scripts/check_docs.py"],
    }
    logs = {}
    for filename, args in commands.items():
        result = subprocess.run([sys.executable, *args], cwd=ROOT, text=True, capture_output=True)
        logs[filename] = f"command: python {' '.join(args)}\nsource_commit: {commit}\nexit_code: {result.returncode}\n" + result.stdout + result.stderr
        if result.returncode:
            raise SystemExit(logs[filename])
    runs = []
    for scenario in ("good", "known-bad", "timeout"):
        result = subprocess.run([sys.executable, "scripts/run_demo.py", "--scenario", scenario],
                                cwd=ROOT, text=True, capture_output=True, check=True)
        path = Path(result.stdout.strip())
        report = json.loads((path / "report.json").read_text(encoding="utf-8"))
        if report["commit"] != commit or report["working_tree_dirty_at_start"] is not False:
            raise SystemExit("Source provenance changed during collection; keep runs for diagnosis.")
        runs.append({"scenario": scenario, "run_id": report["run_id"],
                     "path": path.relative_to(ROOT).as_posix(), "actual_attempts": report["actual_attempts"],
                     "stop_reason": report["stop_reason"], "uncovered": report["uncovered"],
                     "conclusions": {r["test_id"]: r["conclusion"] for r in report["results"]}})
    validation = ROOT / "evidence" / "validation"
    validation.mkdir(exist_ok=True)
    for filename, content in logs.items():
        (validation / filename).write_text(content, encoding="utf-8", newline="\n")
    manifest = {"submission": "first-submission-v0.1", "source_commit": commit,
                "created_at": datetime.now(timezone.utc).isoformat(),
                "source": "fixture_demo", "evidence_level": "OBSERVED", "human_signoff": "pending",
                "validation": {name: {"exit_code": 0, "sha256": hashlib.sha256((validation / name).read_bytes()).hexdigest()}
                               for name in logs}, "runs": runs}
    (ROOT / "evidence" / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
