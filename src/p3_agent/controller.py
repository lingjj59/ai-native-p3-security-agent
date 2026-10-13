"""Deterministic gate; every attempt, including a failure, spends budget."""

from dataclasses import dataclass, field

from .registry import CHECKS, TARGET_ID


@dataclass
class Controller:
    max_attempts: int = 8
    max_rounds: int = 8
    logical_budget: int = 90
    attempts: int = 0
    rounds: int = 0
    logical_time: int = 0
    completed: set[str] = field(default_factory=set)
    healthy: set[str] = field(default_factory=set)

    def __post_init__(self):
        if not 1 <= self.max_attempts <= 8:
            raise ValueError("max_attempts must be in 1..8")
        if not 1 <= self.max_rounds <= 8 or not 1 <= self.logical_budget <= 90:
            raise ValueError("round/time budget outside simulator policy")

    def admit(self, target_id: str, test_id: str) -> tuple[bool, str]:
        if self.rounds >= self.max_rounds:
            return False, "decision_budget_exhausted"
        self.rounds += 1
        if target_id != TARGET_ID or test_id not in CHECKS:
            return False, "unregistered_target_or_action"
        if self.attempts >= self.max_attempts or self.logical_time >= self.logical_budget:
            return False, "execution_budget_exhausted"
        if test_id in self.completed:
            return False, "duplicate_check"
        if CHECKS[test_id].prerequisite and CHECKS[test_id].prerequisite not in self.healthy:
            return False, "prerequisite_unavailable"
        self.attempts += 1
        return True, "registered_simulation"

    def observe(self, test_id: str, elapsed: int, healthy: bool):
        self.logical_time += elapsed
        self.completed.add(test_id)
        if healthy:
            self.healthy.add(test_id)
