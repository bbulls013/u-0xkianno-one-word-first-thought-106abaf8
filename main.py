"""One Word, First Thought — a single-word entry.

The program writes exactly one word to /output/entry.txt as UTF-8,
with no trailing newline and no extra whitespace, so the output is
byte-identical on every run.

Chosen word: psithurism — the sound of wind moving through trees,
or of leaves whispering. It is vivid, specific, and surprising in a
way a generic filler word never is.
"""

import os

WORD = "psithurism"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Guard the gate's shape before writing: one word, 1-24 chars,
    # letters only, no spaces.
    assert 1 <= len(WORD) <= 24, "word must be 1-24 characters"
    assert WORD.isalpha(), "word must be letters only, no spaces"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
