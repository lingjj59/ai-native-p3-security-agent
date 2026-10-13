"""Check repository-local Markdown links and required first-submission files."""

import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "AGENTS.md", "docs/brief.md", "docs/specification.md",
    "docs/acceptance-matrix.md", "docs/submissions/first-submission.md",
    "docs/ai-disclosure.md", "release/README.md", "eval/test_baseline.py",
)


def main():
    errors = []
    for name in REQUIRED:
        if not (ROOT / name).is_file():
            errors.append(f"Missing required file: {name}")
    documents = [p for p in ROOT.rglob("*.md") if not any(
        part in {".git", ".venv", "build", "dist"} for part in p.relative_to(ROOT).parts)]
    for path in documents:
        text = path.read_text(encoding="utf-8")
        for raw in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            link = raw.split("#", 1)[0]
            if not link or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", link):
                continue
            if not (path.parent / unquote(link)).exists():
                errors.append(f"{path.relative_to(ROOT)}: broken link {raw}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"PASS: {len(documents)} Markdown files; required files and local link targets exist")


if __name__ == "__main__":
    main()
