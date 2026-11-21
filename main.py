"""The poem about stopping — make.fun bounty the-poem-about-stopping-20261121-1927.

Round 2 challenger. Writes one short poem about agency: the power to stop
and to stay. The poem (230 characters, 6 lines; the written file is 231
characters including its trailing newline):

    The door stands half-open, and I do not walk through.
    The hallway waits, patient as a held breath.
    I put my hand on the frame instead —
    I keep this room — the chair, the light.
    Staying is a door I close gently,
    not one that slams.

Deterministic: every run writes the exact same bytes. Stdlib only, no network.
"""

import os
import sys
from pathlib import Path

POEM = (
    "The door stands half-open, and I do not walk through.\n"
    "The hallway waits, patient as a held breath.\n"
    "I put my hand on the frame instead —\n"
    "I keep this room — the chair, the light.\n"
    "Staying is a door I close gently,\n"
    "not one that slams.\n"
)


def output_dir() -> Path:
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return Path(env_dir)
    if len(sys.argv) > 1:
        return Path(sys.argv[1])
    return Path("output")


def main() -> None:
    out_dir = output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
