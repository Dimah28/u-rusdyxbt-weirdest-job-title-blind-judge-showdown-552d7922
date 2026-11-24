#!/usr/bin/env python3
"""Write one job title to /output/entry.txt.

Deterministic, stdlib only, no network. One line, 48 characters.

Why this title wins its pairings: it is a real-sounding senior role
("Chief ... Officer") with one hilariously specific twist -- a human
whose whole job is apologising to shoppers on behalf of the
self-checkout machines that beep, freeze, and accuse them of stealing.
Anyone who has ever fought a self-checkout can picture this person
instantly, and the apology lands on the first read.
"""

import os

TITLE = "Chief Apology Officer for Self-Checkout Machines"


def validate_title(title: str) -> None:
    """Enforce the competition gates: 1-60 characters, one non-blank line."""
    if not 1 <= len(title) <= 60:
        raise ValueError(f"title is {len(title)} characters, must be 1-60")
    if "\n" in title or not title.strip():
        raise ValueError("title must be a single non-blank line")


def main() -> None:
    validate_title(TITLE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TITLE)
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
