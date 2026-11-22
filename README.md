[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/Vikkry88/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/Vikkry88/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

# World News in One Picture — Saturday 21 November 2026 (v2: 42 stories, 7 regions, world map, UTC timeline)

A dense newspaper front-page image that sums up the world's news of Saturday
21 November 2026 in a single picture, for the make.fun `news-image-20261121`
competition.

## What the image shows (v2)

The masthead reads "THE WORLD TODAY — Saturday 21 November 2026 • 42 stories
• 7 regions". A "how to read" strip explains the numbered map pins and the
confidence labels. A UTC timeline (03:34–23:25 first-reported times) and a
"day in numbers" strip (9–6 ICJ vote, 275 drones CLAIM, €1bn EU aid, M6.7
Peru, S&P −3.7% to 6,910, Nikkei −5.06%, gold $3,515 −4.62%, Brent ~$90,
4.1 km incursion, 6,800 buildings, 35% by 2035, $120bn dropped) run under it.

Three illustrated lead stories:

- **1 Shenzhen fallout** — Trump defends calling Putin "friend"; Zelensky
  calls Putin a "killer"; nuclear-risk talks agreed after the 19 Nov summit;
  no Ukraine breakthrough.
- **2 Ukraine war widens** — Kryvyi Rih hit (2 dead), Russian ship burning
  off Finland after a Saturday drone hit, Moscow claims 275 drones downed,
  EU sends €1bn.
- **3 COP31 overtime, Antalya** — fossil fuels cut from the draft, $120bn
  adaptation goal dropped, 35% electricity by 2035 kept; France and Panama
  push back; nearly 200 countries, no deal yet on 21 Nov.

Twelve picture cards (4–15): Myanmar rejects the 9–6 ICJ Rohingya genocide
ruling; two tankers hit off Khasab (UKMTO 215/216, mine claim disputed);
Peru M6.7; UK–EU three deals; Geneva AI-weapons talks (~100 back binding
rules by 2028); Palisades arson conviction (12 dead, 6,800 buildings);
Bolsonaro in ICU; Turkey seizes Sozcu TV; Rikers Island to close by 2032;
AI selloff (S&P −3.7%); Estonia shuts Russia crossings Dec 1; Ladakh's first
elections since 2019.

Twenty-seven one-line briefs (16–42) grouped by region — North America,
Latin America, Europe, Middle East & Gulf, Africa, Asia-Pacific, Global —
each with a source tag and a REPORTED / FORECAST / CLAIM / DISPUTED label.
A world map carries 42 numbered pins matching the story numbers. A DATE
CHECK box lists stories excluded as other days' news (Shenzhen summit itself
19 Nov, the 110-missile barrage night 19–20 Nov, the ICJ judgment delivered
19 Nov, the EU €1bn Council decision of 20 Nov 15:50, the 20 Nov "Chapo
Isidro" arrest, the OFAC list published 20 Nov, and 22 Nov developments).

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
