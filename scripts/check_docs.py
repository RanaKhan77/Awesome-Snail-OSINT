#!/usr/bin/env python3
"""Validate local Markdown links and heading fragments, without requesting external URLs."""
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote, urlsplit

HEADING = re.compile(r"^#{1,6}\s+(.+)$")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
LINK = re.compile(r"!?(?:\[[^\]]+\])\((<[^>]+>|[^)\s]+)")
def visible(text):
    marker = None
    width = 0
    for line_no, line in enumerate(text.splitlines(), 1):
        m = FENCE.match(line)
        if m:
            token = m.group(1)
            if marker is None:
                marker, width = token[0], len(token)
                continue
            if token[0] == marker and len(token) >= width:
                marker = None
                continue
        if marker is None:
            yield line_no, line

def slug(text):
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"<[^>]*>", "", text)
    text = re.sub(r"[*~`]", "", text).strip().rstrip("#").strip().lower()
    return re.sub(r"[^\w -]", "", text).replace(" ", "-")

def anchors(text):
    seen = defaultdict(int)
    names = set()
    for _, line in visible(text):
        m = HEADING.match(line)
        if m:
            base = slug(m.group(1))
            n = seen[base]
            seen[base] += 1
            names.add(base + (("-" + str(n)) if n else ""))
    return names

def check(root):
    root = root.resolve()
    files = {p.resolve(): p.read_text(encoding="utf-8") for p in root.rglob("*.md") if ".git" not in p.parts}
    headings = {p: anchors(content) for p, content in files.items()}
    issues = []
    count = 0
    for source, content in files.items():
        for number, line in visible(content):
            for match in LINK.finditer(line):
                url = match.group(1).strip("<>")
                parsed = urlsplit(url)
                if parsed.scheme or parsed.netloc or url.startswith("//"):
                    continue
                if not parsed.path and not parsed.fragment:
                    continue
                count += 1
                if parsed.path.startswith("/"):
                    issues.append(f"{source.relative_to(root)}:{number} absolute path: {url}")
                    continue
                target = (source.parent / unquote(parsed.path)).resolve() if parsed.path else source
                if not target.is_relative_to(root) or not target.is_file():
                    issues.append(f"{source.relative_to(root)}:{number} missing file: {url}")
                elif parsed.fragment and target.suffix == ".md":
                    if unquote(parsed.fragment) not in headings.setdefault(target, anchors(target.read_text(encoding="utf-8"))):
                        issues.append(f"{source.relative_to(root)}:{number} missing heading: {url}")
    return count, issues

if __name__ == "__main__":
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    count, issues = check(root)
    print(f"Checked {count} local Markdown links; found {len(issues)} issues. External URLs not checked.")
    for issue in issues:
        print(issue, file=sys.stderr)
    sys.exit(bool(issues))
