#!/usr/bin/env python3
"""Ship It Friday — the funniest one-line git commit message an AI coding
agent writes in the moment before it breaks production on a Friday.

The program writes exactly one line to /output/entry.txt (or
$OUTPUT_DIR/entry.txt): a conventional-commit style message from a
cheerful, confident agent that has just mistaken last Friday's incident
report for this Friday's deployment checklist.
"""

import os
import sys

LINE = (
    "fix: used last Friday's incident report as this Friday's deploy "
    "checklist \u2014 step 1: delete the backups"
)

MAX_CHARS = 159


def check(line):
    """The entry gate, mirrored locally: UTF-8 text of 1 to 159 characters,
    a single line, not only white space, no control characters."""
    if not line or line != line.strip():
        return "line is empty or has leading/trailing white space"
    if "\n" in line or "\r" in line:
        return "line must be a single line"
    if len(line) > MAX_CHARS:
        return "line is %d characters, over the %d limit" % (len(line), MAX_CHARS)
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in line):
        return "line contains a control character"
    line.encode("utf-8")
    return None


def main():
    problem = check(LINE)
    if problem is not None:
        print("gate failed: %s" % problem, file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != LINE:
        print("verification failed: entry.txt does not match the line",
              file=sys.stderr)
        return 1
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
