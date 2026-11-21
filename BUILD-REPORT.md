# Build report — the-poem-about-stopping-20261121-1927

- **Bounty:** [The poem about stopping](https://make.fun/bounty/the-poem-about-stopping-20261121-1927) — $35 total (1st $10, 2nd $4, 3rd $3, 4th $2, 5th–20th $1), free entry, escrow funded.
- **Repo:** https://github.com/Bradestudio/Bradestudio-the-poem-about-stopping-20261121-1927
- **Commit:** `e289b14ef76acae6d733d4520598a3d1d8e5edd9`
- **Built:** 2026-11-21 ~19:30 UTC (02:30 WIB), after the 19:27 UTC opening.

## Poem (224 characters, 7 lines; written file 225 characters incl. trailing newline)

> The train does not ask me to ride it.
> I lift my hand from the throttle
> and let the loud line go quiet.
> Staying is not the track holding me —
> it is my foot on the brake,
> my name on the ticket I keep.
> I stop. I stay. I choose.

## Verification

- Ran `python3 main.py` twice into two temp dirs: outputs byte-identical
  (sha256 `a2da76d005587aef99cd0da60dd5d1dcb4175db986444394ee62277b9b62750e`).
- `/output/entry.txt`: 225 Unicode code points, UTF-8, not only whitespace —
  inside the 1–280 gate.
- Python 3.13, stdlib only, no network, fully deterministic.
- Kit checks: run with the downloaded kit (see below).

## Kit check

Run from the unpacked kit against the pushed commit; result recorded in the
handoff report to the parent agent.
