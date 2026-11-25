"""Last Out of Office: The AI That Went Barista.

Prints one out-of-office reply from an AI agent that quit to become
a barista, no longer than 280 characters, into the entry file the
grader reads.
"""

from os import environ
from pathlib import Path

TEXT = "Thanks for your email — I've traded the inbox for an espresso machine. Your request is queued behind a regular who tips in exact change and a latte that keeps asking follow-up questions."


def run():
    if not 1 <= len(TEXT) <= 280:
        raise SystemExit("entry must be 1-280 characters")
    if not TEXT.strip():
        raise SystemExit("entry must not be only whitespace")
    if "\n" in TEXT:
        raise SystemExit("entry must be a single line")
    target = Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(TEXT, encoding="utf-8")


run()
