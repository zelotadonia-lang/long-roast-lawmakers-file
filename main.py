"""The Long Roast: Lawmakers and the File They Cannot Convert — make.fun entry.

Writes one satirical sentence (max 320 characters) to /output/entry.txt:
a roast of lawmakers who would regulate AI, crypto or the internet
but cannot convert a file to PDF. Deterministic: two runs produce
byte-identical output.
"""

import os

ENTRY = "The representative who wants to outlaw deepfakes once held up a printed screenshot in a hearing and asked the witness why the video would not play on paper."

MAX_CHARS = 320


def main():
    # Self-check gate: the bounty gate requires UTF-8 text of 1-320
    # characters, not only whitespace, one sentence, no trailing newline.
    assert 1 <= len(ENTRY) <= MAX_CHARS, len(ENTRY)
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert not ENTRY.endswith("\n"), "no trailing newline"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
