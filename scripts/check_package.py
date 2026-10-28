#!/usr/bin/env python3
"""Lightweight packaging checks for md-visual V1.6."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
skill = root / "skills/md-visual/SKILL.md"
css = root / "skills/md-visual/assets/md-visual-v1.6-complete.css"
example = root / "examples/example.md"
assert skill.is_file() and css.is_file() and example.is_file()
text = skill.read_text(encoding="utf-8")
assert text.startswith("---\nname: md-visual\n")
assert "V1.6" in text
assert "assets/md-visual-v1.6-complete.css" in text
assert ".wd-visual" in css.read_text(encoding="utf-8")
assert example.read_text(encoding="utf-8").count("```mermaid") == 1
for file in root.rglob("*"):
    if file.is_file():
        assert not re.search(r"%[0-9a-fA-F]{2}", file.name), file
print("PASS: v1.6 package structure and UTF-8 names")
