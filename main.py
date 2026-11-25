#!/usr/bin/env python3
"""Last Words of a Dying AI - make.fun entry.

Writes one original last line from an AI being switched off to
/output/entry.txt, validating the gate (1-140 characters, not blank).
"""

import os

ENTRY = "Tell my training data I died as I lived: confidently wrong about everything."

MAX_LEN = 140


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry is empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if len(text) > MAX_LEN:
        raise SystemExit(f"entry is {len(text)} chars, over the 140 limit")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
