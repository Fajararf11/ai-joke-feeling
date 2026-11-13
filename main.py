"""make.fun ai-joke-03 entry.

Writes one fixed one-liner about AI coding agents to entry.txt. Output is
deterministic: standard library only, no network, clock, randomness, or
locale dependence.
"""

import os
from pathlib import Path

JOKE = (
    "Two hours into the refactor my agent reported progress as a feeling. "
    "Forty files open, none closed, and the feeling was nearly there."
)


def write_entry(out_dir):
    """Create out_dir, write JOKE plus one LF-terminated newline to entry.txt, return the path."""
    entry = Path(out_dir) / "entry.txt"
    entry.parent.mkdir(parents=True, exist_ok=True)
    entry.write_text(JOKE + "\n", encoding="utf-8", newline="\n")
    return entry


def main():
    """Write the entry under MAKEFUN_OUTPUT_DIR (default /output) and print its path."""
    print(write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"))


if __name__ == "__main__":
    main()
