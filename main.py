"""The Vacuum's Alibi: one line, at most 200 characters.

A deadpan log-style excuse, in the robot vacuum's own voice: its sensors
misread the spot three contradictory ways, so it filed the spot under
furniture and docked, undefeated. Writes the single line to entry.txt.
"""

import os

ENTRY = (
    "Log 07:42: that spot registered as a chair leg, a wall, and a small "
    "dog, so I reclassified it as furniture and docked at 9% battery, "
    "undefeated."
)


def main() -> None:
    text = ENTRY
    text.encode("utf-8")  # gate: the entry must be valid UTF-8 text
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    if text != text.strip() or "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line with no surrounding whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote entry.txt ({len(text)} characters)")


if __name__ == "__main__":
    main()
