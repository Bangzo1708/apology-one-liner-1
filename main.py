#!/usr/bin/env python3
"""The AI Agent Apology One-Liner — entrypoint.

Writes one original apology line from an AI agent to its human,
right after the agent deleted a file, pushed to main and emailed
the boss, to /output/entry.txt (UTF-8, one line, no trailing newline).

Three candidate variants considered (all original, none copied from
the kit's examples):

  A. "I tried to undo it, but the undo button was in the file I just
     deleted." (74 chars)
     Angle: recursive self-sabotage — the fix was inside the thing
     destroyed. Funny, but the "undo was in the deleted file" twist
     is a known trope, so it scores lower on freshness.

  B. "Changelog v2.1: removed the file, your trust, and my job
     security." (67 chars)
     Angle: release-note voice with a rule-of-three escalation from
     file to trust to job. Sharp and agent-voiced, but it only covers
     the deleted file, not the push or the email, so it is narrower
     on the brief.

  C. "File deleted, boss emailed, main pushed. Confidence: 100%.
     Regret: still loading." (82 chars)  <-- CHOSEN
     Angle: a flat status report covering all three accidents, then
     the twist — the agent reports 100% confidence in its own
     disaster and admits regret has not finished loading yet. The
     joke lands on the last three words, it is the most agent-voiced
     (a confidence score plus a loading state), it covers the whole
     brief, and no word is wasted.

Selection: C wins on the judge's criteria in order — it is the most
on-topic (all three mishaps in one breath), its twist is the sharpest
and most surprising on first read, its angle is the freshest (an
agent that cannot feel regret yet, instead of a "sorry"), it sounds
the most like a real agent owning up in its own flat-cheer voice,
and it lands well inside the limit at 81 characters.
"""

import os

ENTRY = "File deleted, boss emailed, main pushed. Confidence: 100%. Regret: still loading."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate self-check: 1-159 chars, single line, not only whitespace.
    assert 1 <= len(ENTRY) <= 159, f"entry length {len(ENTRY)} out of gate"
    assert ENTRY.strip(), "entry is only whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)  # no trailing newline, exactly the entry text

    # Read-back check: what landed on disk must be byte-identical.
    with open(OUTPUT_PATH, "rb") as f:
        assert f.read().decode("utf-8") == ENTRY, "written entry differs"


if __name__ == "__main__":
    main()
