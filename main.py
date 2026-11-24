#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest - make.fun bounty entry.

Writes a short, funny rant about the self-checkout machine accusing
an honest shopper of theft, to /output/entry.txt (the file the
make.fun harness grades).
"""

import os

ENTRY = "The self-checkout machine has accused me of stealing my own groceries again. I scanned the milk, I bagged the milk, and still it froze, flashed \u2018unexpected item in the bagging area,\u2019 and summoned a teenager to watch me re-scan the milk like a suspect. I came here to buy dinner, not to audition for a crime I did not commit in front of an audience of impatient strangers."

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
