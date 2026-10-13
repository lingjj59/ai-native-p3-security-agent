"""Pure in-memory simulator. It has no URL, shell or credential interface."""

from copy import deepcopy

from .registry import CHECKS


class Simulator:
    def __init__(self, fixture: dict):
        self.fixture = deepcopy(fixture)
        self.calls: list[str] = []

    def execute(self, test_id: str) -> dict:
        check = CHECKS[test_id]
        self.calls.append(test_id)
        result = {
            "request_id": f"sim-request-{len(self.calls):03d}",
            "status_code": check.expected_status,
            "body": check.canary if check.expected_status == 200 else "access denied",
            "tool_error": None,
            "logical_seconds": 1,
        }
        result.update(deepcopy(self.fixture.get("overrides", {}).get(test_id, {})))
        return result
