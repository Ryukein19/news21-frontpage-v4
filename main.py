#!/usr/bin/env python3
"""The Saturday Front Page — 21 November 2026.

Copies the shipped front-page image to /output/entry.png.
Standard library only; no network access.
"""
import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    print(f"wrote {dst} ({size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
