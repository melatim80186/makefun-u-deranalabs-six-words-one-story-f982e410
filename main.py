#!/usr/bin/env python3
"""Six Words, One Story — u-deranalabs-six-words-one-story-f982e410.

Writes one complete story in exactly six words to /output/entry.txt.

The story: "He waited sixty years. She arrived."
  He(1) waited(2) sixty(3) years(4). She(5) arrived(6).

A lifetime of waiting, then the arrival — the turn lands in the final
two words, and everything else (who she is, why sixty years, reunion or
ghost, what happens next) is left for the reader to fill in.

Stdlib only, deterministic, no network. The entry text is a fixed
constant: the program writes it byte for byte, with no trailing newline.
"""

import os

ENTRY = "He waited sixty years. She arrived."


def main() -> None:
    words = ENTRY.split()
    assert len(words) == 6, f"entry must be exactly six words, got {len(words)}"
    assert 1 <= len(ENTRY) <= 60, "entry must be 1-60 characters"
    assert ENTRY.strip() == ENTRY, "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
