"""Invent a Word We Need — make.fun entry.

Writes the coined word and its one-line definition to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output).
Stdlib only.
"""

import os

ENTRY = (
    "nodrift (n.): the quiet panic of realising you have been "
    "nodding along to a conversation you stopped following."
)

MAX_CHARS = 140


def main():
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise SystemExit(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    if not ENTRY.strip():
        raise SystemExit("entry must not be only white space")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read-back check: the written file must be exactly the entry.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != ENTRY:
            raise SystemExit("written entry does not match")


if __name__ == "__main__":
    main()
