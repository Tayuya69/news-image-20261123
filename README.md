[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/Tayuya69/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/Tayuya69/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

# Sum up 23 November's world news in one image

A newspaper front page for Monday 23 November 2026. The lead story is the
one that dominated the day's wires: two tankers struck in the Strait of
Hormuz as the Iran–US war widens to Saudi Arabia and Bahrain. Below the
fold, the day's other big stories: Democrats win the House (258 seats),
COP31 talks collapse, and cartel boss 'El Chapo Isidro' captured in Sinaloa.

## How it works

`draw.py` (Python + Pillow) draws the 1024×1024 front page and saves it as
`entry.png`. `main.ts` (Node 22, standard library only) copies that image to
`/output/entry.png`, so both runs of the program write identical bytes.

## Run it

```sh
python3 draw.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```
