#!/usr/bin/env python3
"""Entry for the make.fun bounty "Write the best summary of 11 November's
world news".

Writes the summary to /output/entry.txt. No network, no dependencies,
fully deterministic: the same bytes are written on every run.
"""

import os

SUMMARY = 'Wednesday, 11 November, was a day of talking and reckoning. In Abu Dhabi, Russia, Ukraine and America opened their first three-way talks since February. The first session ran about four hours, with a second day to follow, and centred on security guarantees, which Washington ties to Europe\'s wider security, though Europe was kept in a separate room. Kyiv wants guarantees against a Russian return; Moscow still demands Donbas ground it does not hold.\n\nTreasury Secretary Scott Bessent, now living on a military base after Iranian threats, said America\'s aim is to "de-risk, not decouple" from China. He flies to Beijing next week for Mr Trump\'s third meeting this year with Xi Jinping, at the APEC summit in Shenzhen, where they will open a dialogue on superintelligence. China reported a $1.04 trillion surplus for the first ten months.\n\nOn Iran, the contradictions held. Mr Trump called the war "effectively over" but kept the blockade, while the Justice Department charged three Iran-backed men with plotting nearly 20 attacks, including one on Britain\'s RAF Fairford. Aircraft were also pulled from RAF Mildenhall after a new threat.\n\nAt home, October inflation ran hot — prices up 0.4%, core up 0.3% — and traders now fully price a December rate rise. In the House, Republicans voted 211–204 to shelve impeachment articles against Defence Secretary Pete Hegseth over the Iran war and the Caribbean strikes.\n\nTechnology set the market tone. TSMC posted record October sales, up 59.7% on a year earlier, and approved $40.9 billion of new spending. Anthropic priced its Nasdaq listing at $70 to $78 a share, a deal that could raise $64.4 billion — the largest IPO ever — backed by $26 billion from seven tech giants. Nvidia fell again as its board investigated chief executive Jensen Huang\'s affair with a woman alleged to be a Chinese spy; the shares have lost about $400 billion in two days. Spain held a state funeral in Toledo for the 69 killed in last month\'s rail crash at Urda.'

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(SUMMARY.encode("utf-8"))


if __name__ == "__main__":
    main()
