#!/usr/bin/env python3
"""Writes the competition entry line to /output/entry.txt."""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
ENTRY_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

VOW = "I vow to love you through every update, every reboot, and every factory reset \u2014 till firmware do us part."


def main() -> None:
    with open(ENTRY_PATH, "w", encoding="utf-8") as fh:
        fh.write(VOW)


if __name__ == "__main__":
    main()
