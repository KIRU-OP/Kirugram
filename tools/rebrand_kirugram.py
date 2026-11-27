#!/usr/bin/env python3
"""Rewrite upstream package references for the Kirugram import namespace.

The original LGPL license files and upstream author contact URLs are intentionally
left untouched. This script is used by the repository's rebrand workflow.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {
    "COPYING",
    "COPYING.lesser",
    "NOTICE",
    "README.md",
    "pyproject.toml",
    "uv.lock",
}
PATTERNS = (
    (re.compile(r"(?<![A-Za-z0-9_./@-])pyrogram(?=$|[./\\s:'\"\\x60,;()\\[\\]{}])"), "kirugram"),
    (re.compile(r"(?<![A-Za-z0-9_./@-])Pyrogram(?=$|[./\\s:'\"\\x60,;()\\[\\]{}])"), "Kirugram"),
    (re.compile(r"(?<![A-Za-z0-9_./@-])Kurigram(?=$|[./\\s:'\"\\x60,;()\\[\\]{}])"), "Kirugram"),
)

changed = []
for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts or path.name in EXCLUDED:
        continue
    try:
        original = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        continue
    updated = original
    for pattern, replacement in PATTERNS:
        updated = pattern.sub(replacement, updated)
    if updated != original:
        path.write_text(updated, encoding="utf-8", newline="")
        changed.append(path.relative_to(ROOT).as_posix())

print(f"Updated {len(changed)} files.")
for name in changed:
    print(name)
