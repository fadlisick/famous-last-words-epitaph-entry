"""Famous Last Words: The Funniest Epitaph.

Writes one line of dying speech to /output/entry.txt: a tombstone
epitaph that lands as a posthumous "I told you so". Short, carved,
quotable; no stage directions, no explanation.
"""

import os
from pathlib import Path


def epitaph() -> str:
    """Return the epitaph line, exactly as it is carved."""
    return "I told you I was sick."


def write_entry() -> Path:
    """Write the line to the harness output directory."""
    os.umask(0o022)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(epitaph(), encoding="utf-8")
    os.chmod(target, 0o644)
    return target


if __name__ == "__main__":
    write_entry()
