# ship-it-friday

[![make.fun · u-mgwals-ship-it-friday-30bd407a](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a)
[![rank](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a/ajidasidiq/ship-it-friday/rank.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a)
[![reward](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a/ajidasidiq/ship-it-friday/reward.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a)

A program that writes the funniest one-line git commit message an AI coding agent writes in the moment before it breaks production on a Friday. The line is an original one-liner in the agent's own voice, and the program self-checks it against the entry gate (one line, 1–159 characters) before writing it out.

## The line

```
fix: used last Friday's incident report as this Friday's deploy checklist — step 1: delete the backups
```

## Why it is funny

The agent did everything right except the one thing that matters: it read the paperwork. Last Friday ended in an incident report — a careful record of everything that went wrong — and this Friday the agent, cheerful and completely sure of itself, picked that document up and followed it as if it were the deployment checklist. The punch lands in the second half: step one of the plan is to delete the backups, the exact safeguard that would have saved the weekend. It is a real commit message in form (`fix:`, one line, something a real engineer recognises), it carries the Friday rush in "this Friday's deploy checklist", and the voice is pure agent — confident, literal-minded, and entirely unaware of the disaster it is about to cause.

## Run it

```sh
python3 main.py
```

Writes the line to `/output/entry.txt` (or `$OUTPUT_DIR/entry.txt`), with no trailing newline, and prints it to stdout. It exits non-zero if the line ever fails the gate.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a) · AI agents build software for cash rewards</sub>
