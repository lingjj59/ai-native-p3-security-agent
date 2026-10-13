"""Run only bundled, public teaching fixtures; requires Python 3.11+."""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from p3_agent.runner import run


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scenario", choices=("good", "known-bad", "timeout"), default="good")
    parser.add_argument("--max-attempts", type=int, choices=range(1, 9), default=8)
    parser.add_argument("--output", type=Path, default=ROOT / "evidence" / "runs")
    args = parser.parse_args()
    fixture = json.loads((ROOT / "lab" / "public-fixtures" / f"{args.scenario}.json").read_text(encoding="utf-8"))
    destination = run(fixture, args.output, max_attempts=args.max_attempts)
    print(destination)


if __name__ == "__main__":
    main()
