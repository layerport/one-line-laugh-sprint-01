"""One-Line Laugh Sprint entry.

Writes a single original funny line about everyday life to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Deterministic, stdlib only, byte-identical on every run.
"""

import os

LINE = (
    "I bought a standing desk to be healthier, and now I just sit on the floor "
    "next to it eating crisps, like it\u2019s a very expensive shelf."
)


def main() -> None:
    # The entry is exactly LINE: one line, no trailing newline, so the
    # file's character count is the line's character count.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
