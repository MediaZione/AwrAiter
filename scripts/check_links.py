#!/usr/bin/env python3
"""Check that every relative link and image in the Markdown files resolves.

External links are not fetched: a docs repo should not go red because someone
else's site is briefly down. Anchors are checked against the headings of the
target file, since a stale `#section` is the failure that actually happens here.
"""
from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HEADING = re.compile(r"^#{1,6}\s+(.*)$", re.MULTILINE)
FENCE = re.compile(r"```.*?```", re.DOTALL)


def slugify(heading: str) -> str:
    text = re.sub(r"[`*_]", "", heading).strip().lower()
    text = "".join(c for c in text if unicodedata.category(c)[0] in "LNZP" or c == "-")
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    return re.sub(r"[\s]+", "-", text).strip("-")


def anchors_of(path: Path) -> set[str]:
    body = FENCE.sub("", path.read_text(encoding="utf-8"))
    return {slugify(h) for h in HEADING.findall(body)}


def main() -> int:
    problems: list[str] = []
    for md in sorted(ROOT.rglob("*.md")):
        if ".git" in md.parts:
            continue
        body = FENCE.sub("", md.read_text(encoding="utf-8"))
        for target in LINK.findall(body):
            if target.startswith(("http://", "https://", "mailto:", "tel:")):
                continue
            rel, _, anchor = target.partition("#")
            resolved = md if not rel else (md.parent / rel)
            if rel and not resolved.exists():
                problems.append(f"{md.relative_to(ROOT)}: missing target {target}")
                continue
            if anchor and resolved.is_file() and resolved.suffix == ".md":
                if anchor.lower() not in anchors_of(resolved):
                    problems.append(f"{md.relative_to(ROOT)}: no heading for {target}")

    for problem in problems:
        print(problem)
    print(f"{len(problems)} broken link(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
