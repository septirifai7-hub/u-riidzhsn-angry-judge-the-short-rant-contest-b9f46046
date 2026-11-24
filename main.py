#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest - make.fun bounty entry.

Writes a short, funny rant about the self-checkout machine accusing
an honest shopper of theft, to /output/entry.txt (the file the
make.fun harness grades).

The rant itself lives in ENTRY_RANT below; get_entry() returns it
unchanged, and write_entry() is responsible for creating the output
directory and writing the file, so main() stays a thin entrypoint.
"""

import os

# The graded rant. Do not edit the wording.
ENTRY_RANT = "The self-checkout machine has accused me of stealing my own groceries again. I scanned the milk, I bagged the milk, and still it froze, flashed \u2018unexpected item in the bagging area,\u2019 and summoned a teenager to watch me re-scan the milk like a suspect. I came here to buy dinner, not to audition for a crime I did not commit in front of an audience of impatient strangers."

# Backwards-compatible alias for the entry text.
ENTRY = ENTRY_RANT


def get_entry() -> str:
    """Return the rant exactly as it should appear in entry.txt."""
    return ENTRY_RANT


def write_entry(out_dir: str) -> str:
    """Write the rant to entry.txt inside out_dir; return the path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(get_entry())
    return path


def main() -> None:
    # The harness sets MAKEFUN_OUTPUT_DIR; fall back to /output so the
    # entry still lands in the graded location when run by hand.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
