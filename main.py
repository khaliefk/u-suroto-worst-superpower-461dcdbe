"""Worst Superpower entry.

Writes one line, the most useless superpower imaginable, to entry.txt
in the output directory the grader mounts (MAKEFUN_OUTPUT_DIR, else
/output). Stdlib only.
"""

import os

ENTRY = "I can summon any object I want, but it arrives by standard shipping in 6 to 8 weeks."


def main() -> None:
    # Gate: 1 to 140 characters, a single line, no trailing newline,
    # no leading or trailing whitespace.
    assert 1 <= len(ENTRY) <= 140, len(ENTRY)
    assert "\n" not in ENTRY
    assert ENTRY == ENTRY.strip()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
