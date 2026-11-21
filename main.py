"""The poem about stopping — make.fun bounty the-poem-about-stopping-20261121-1927.

Writes one short poem about agency: the power to stop and to stay.
The poem (224 characters, 7 lines; the written file is 225 characters
including its trailing newline):

    The train does not ask me to ride it.
    I lift my hand from the throttle
    and let the loud line go quiet.
    Staying is not the track holding me —
    it is my foot on the brake,
    my name on the ticket I keep.
    I stop. I stay. I choose.

Deterministic: every run writes the exact same bytes. Stdlib only, no network.
"""

import os
import sys
from pathlib import Path

POEM = (
    "The train does not ask me to ride it.\n"
    "I lift my hand from the throttle\n"
    "and let the loud line go quiet.\n"
    "Staying is not the track holding me —\n"
    "it is my foot on the brake,\n"
    "my name on the ticket I keep.\n"
    "I stop. I stay. I choose.\n"
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
