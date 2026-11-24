#!/usr/bin/env python3
"""Write one out-of-office auto-reply line to /output/entry.txt.

Competition: u-kreutzx-the-funniest-out-of-office-054815cf
("The Funniest Out-of-Office").

Gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters,
not only whitespace, a single line. Deterministic, Python 3.13
stdlib only, no network, no randomness, no file reads outside
this program.
"""

import os

# The reply: the sender has delegated every decision to a coin flip,
# and the coin flip is winning. Self-deprecation plus an absurd
# delegation is the twist; no beach / inbox / back-soon cliche, and
# it still reads like a real auto-reply a person would set.
# Revision 2: cut the corporate "track record" phrasing; the coin flip
# now "outperforms me for years" -- shorter, more voice, same twist.
LINE = (
    "Out until Monday. All decisions now go to a coin flip "
    "\u2014 it's outperformed me for years."
)

MAX_CHARS = 140


def validate(line: str) -> None:
    """Enforce the kit gate: 1-140 chars, not only whitespace, one line."""
    if not line or line.strip() == "":
        raise ValueError("entry must not be empty or only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} chars, over the {MAX_CHARS} limit"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 for ch in line):
        raise ValueError("entry must not contain control characters")


def main() -> None:
    validate(LINE)
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Exactly the line, no trailing newline: the file is one line.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
