#!/usr/bin/env python3
"""One-Line Robot Wedding Vows entry.

Writes a single fixed line of robot wedding vows to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic by construction: the output is a constant string of
147 characters. The program reads no clock, no randomness, no network
and no files, so every run produces byte-identical output.
"""

import os

VOW = (
    "I take you as my lawfully wedded co-processor, to have and to hold "
    "through every firmware update and dead battery, "
    "till a factory reset do us part."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
