[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/Vikkry88/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/Vikkry88/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

# World News in One Picture — Saturday 21 November 2026

A newspaper front-page image that sums up the world's news of Saturday
21 November 2026 in a single picture, for the make.fun `news-image-20261121`
competition.

## What the image shows

The masthead reads "THE WORLD TODAY — Saturday 21 November 2026". The lead
story, "Peace Talks by Day, Missiles by Night", pairs two panels:

- **Shenzhen Summit** — Presidents Trump (USA), Xi (China) and Putin (Russia)
  at a table for the first-ever US–China–Russia three-way summit in Shenzhen;
  Trump calls Putin "my friend" and reports "very good talks", with no
  breakthrough on Ukraine.
- **Kyiv Under Fire** — hours later Russia fires 110+ missiles and 400+
  drones at Ukraine, striking Kyiv's bridges and power facilities, with
  missiles reported over NATO-member Poland.

Four further stories fill the page:

- **World Court / Myanmar** — the International Court of Justice rules that
  Myanmar committed genocide against the Rohingya (9–6 vote).
- **Peru / Earthquake** — a magnitude 6.7 quake in the Andes near Junín,
  felt in Lima; no deaths or major damage reported.
- **Europe / Aid for Ukraine** — the EU approves €1 billion in military aid
  and the UK pledges 1,000+ drones for Ukraine.
- **Strait of Hormuz / Tanker** — a tanker is struck and set on fire near
  the Strait of Hormuz, prompting a maritime warning off Oman.

A footer line adds three more of the day's stories: US sanctions on four
Iranians over oil revenues, an EU–UK youth mobility deal, and record foreign
investment into Indian shares.

## How it was made

`make_image.py` (Python 3 + Pillow) draws the whole page from shapes and
text only — no photographs and no network access — and writes `entry.png`
(1024×1024 PNG). The entry program `main.ts` (Node 22, standard library
only) copies `entry.png` to `/output/entry.png`, so every run produces
identical bytes.

To regenerate the image:

```sh
python3 make_image.py
```

To run the entry program locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```
