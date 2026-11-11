# News summary — 11 November 2026

Entry for the make.fun bounty "Write the best summary of 11 November's
world news" ($200).

## What it is

`main.py` writes a single English-language summary of the world news of
Wednesday, 11 November 2026 to `/output/entry.txt`. The summary is 1,987
characters of flowing narrative (no bullet list), covering the Abu Dhabi
Russia–Ukraine–US talks, the US–China "de-risk, not decouple" line and
Secretary Bessent's move to a military base, the Iran war and the RAF
Fairford plot charges, October US inflation and the December rate outlook,
the House vote shelving the Hegseth impeachment, TSMC's record sales and
$40.9 billion of new spending, Anthropic's $64.4 billion IPO pricing,
Nvidia's slide amid the Jensen Huang probe, and Spain's state funeral for
the 69 victims of the Urda rail crash. Every fact is drawn from reporting
published on 10–11 November 2026.

## How the program works

The summary text is embedded verbatim in `main.py` as the `SUMMARY`
constant (generated from `summary.txt`, which is kept alongside as the
human-readable source). Running the program creates `/output` if needed
and writes the summary as UTF-8 bytes to `/output/entry.txt`. There is no
network access, no third-party dependency, and no randomness: every run
writes the exact same bytes.

## How to run it

```sh
python3 main.py
# writes /output/entry.txt
```

## Files

- `main.py` — the entry program (Python 3.13, stdlib only)
- `summary.txt` — the summary text, byte-identical to the program output
- `README.md` — this file
- `LICENSE` — MIT License
