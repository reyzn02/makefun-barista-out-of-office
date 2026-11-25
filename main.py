#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista.

The program writes a single out-of-office auto-reply, at most 280
characters, from an AI agent that quit to become a barista, to
/output/entry.txt. It uses only the Python standard library, makes no
network calls, and always writes the same bytes.
"""

import os

LINE = (
    "Thanks for your email \u2014 I've traded the inbox for an espresso "
    "machine. Your request is queued behind a regular who tips in exact "
    "change and a latte that keeps asking follow-up questions."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    assert 1 <= len(LINE) <= 280, "line must be 1-280 characters"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "line must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
