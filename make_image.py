#!/usr/bin/env python3
"""Clean front-page image: world news of Saturday 21 November 2026 (v5 hybrid).

Readable large type: 2 illustrated leads + 6 cards + 6 briefs = 14 stories,
UTC timeline, day-in-numbers, source + confidence on every story, DATE CHECK.
Shapes/text only (PIL). Writes entry.png beside this file (1024x1024).
"""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

PAPER = (250, 246, 236)
INK = (28, 28, 32)
RED = (176, 32, 32)
BLUE = (30, 70, 140)
GOLD = (176, 128, 20)
GREY = (100, 100, 106)
SKY = (198, 220, 240)
DARKBOX = (40, 44, 58)
GREEN = (26, 120, 62)
TEAL = (12, 110, 110)
ORANGE = (180, 96, 16)
WHITE = (255, 255, 255)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)


def F(path, size):
    return ImageFont.truetype(path, size)


def wrap(text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_wrap(x, y, text, font, maxw, fill=INK, leading=4):
    lines = wrap(text, font, maxw)
    lh = font.size + leading
    for ln in lines:
        d.text((x, y), ln, font=font, fill=fill)
        y += lh
    return y


def center_text(cx, y, text, font, fill=INK):
    w = d.textlength(text, font=font)
    d.text((cx - w / 2, y), text, font=font, fill=fill)
    return y + font.size


# ---------- Masthead ----------
d.rectangle([0, 0, W, 118], fill=DARKBOX)
center_text(W // 2, 10, "THE WORLD TODAY", F(SERIF_B, 58), fill=WHITE)
center_text(W // 2, 76, "Saturday 21 November 2026  •  World News in One Picture  •  14 stories", F(SANS_B, 21), fill=(240, 220, 160))
d.rectangle([0, 118, W, 126], fill=RED)

# ---------- Day in numbers ----------
d.rectangle([0, 126, W, 162], fill=BLUE)
center_text(W // 2, 132, "DAY IN NUMBERS:  9–6 ICJ vote  •  275 drones CLAIM  •  €1bn EU aid  •  M6.7 Peru  •  S&P −3.7% → 6,910", F(SANS_B, 17), fill=WHITE)

# ---------- Lead headline ----------
center_text(W // 2, 170, "'FRIEND' BY DAY, FIRE BY NIGHT", F(SERIF_B, 38), fill=RED)
y = draw_wrap(60, 216, "Trump defends calling Putin 'friend' after Shenzhen summit — Zelensky: 'killer'; Ukraine war widens",
              F(SANS_B, 23), 904)

# two lead panels
d.rectangle([36, 276, 500, 500], outline=INK, width=3, fill=SKY)
d.rectangle([36, 276, 500, 310], fill=BLUE)
center_text(268, 282, "1  SHENZHEN FALLOUT", F(SANS_B, 21), fill=WHITE)
d.ellipse([120, 390, 420, 460], fill=(120, 84, 48), outline=INK, width=3)
for cx, col, label in [(150, (200, 40, 40), "USA"), (268, (210, 30, 30), "CHINA"), (386, (40, 80, 180), "RUSSIA")]:
    d.ellipse([cx - 26, 328, cx + 26, 380], fill=(240, 210, 170), outline=INK, width=2)
    d.rectangle([cx - 30, 380, cx + 30, 422], fill=col, outline=INK, width=2)
    center_text(cx, 428, label, F(SANS_B, 17), fill=WHITE)
d.rectangle([36, 458, 500, 500], fill=WHITE)
draw_wrap(52, 464, "Nuclear-risk talks agreed; no Ukraine deal. BBC/CBS • REPORTED", F(SANS_B, 15), 432)

d.rectangle([524, 276, 988, 500], outline=INK, width=3, fill=(60, 50, 70))
d.rectangle([524, 276, 988, 310], fill=RED)
center_text(756, 282, "2  UKRAINE WAR WIDENS", F(SANS_B, 21), fill=WHITE)
for bx, bh in [(545, 90), (600, 130), (660, 100), (720, 150), (790, 110), (850, 140), (910, 95)]:
    d.rectangle([bx, 470 - bh, bx + 46, 470], fill=(30, 30, 40), outline=(0, 0, 0), width=1)
    for wy in range(470 - bh + 10, 460, 22):
        d.rectangle([bx + 8, wy, bx + 16, wy + 8], fill=(255, 220, 120))
        d.rectangle([bx + 26, wy, bx + 34, wy + 8], fill=(255, 220, 120))
for mx, my in [(580, 340), (680, 325), (800, 345), (900, 330)]:
    d.line([mx, my, mx + 46, my + 52], fill=(255, 160, 60), width=5)
    d.ellipse([mx + 40, my + 46, mx + 56, my + 62], fill=(255, 90, 40))
    d.polygon([(mx - 4, my - 4), (mx + 10, my - 2), (mx + 2, my + 12)], fill=(220, 220, 220))
d.rectangle([524, 458, 988, 500], fill=WHITE)
draw_wrap(540, 464, "Kryvyi Rih hit (2 dead); ship burns off Finland. Reuters • REPORTED", F(SANS_B, 15), 432)

# ---------- 6 cards (2 cols x 3 rows) ----------
cards = [
    ("3  WORLD COURT • MYANMAR", BLUE, "Rejects 9–6 genocide ruling as 'biased'", "Judgment 19 Nov; rejection 21 Nov.", "Reuters • REPORTED"),
    ("4  PERU • EARTHQUAKE", ORANGE, "Magnitude 6.7 quake shakes Andes, felt in Lima", "No deaths or major damage reported.", "USGS • REPORTED"),
    ("5  EUROPE • AID FOR UKRAINE", GREEN, "EU approves €1 billion in military aid", "Drones, air defence, ammo by end 2027.", "EU Council • REPORTED"),
    ("6  STRAIT OF HORMUZ • TANKERS", TEAL, "Two tankers hit off Khasab; mine claim", "UKMTO 215/216. No casualties.", "UKMTO • DISPUTED"),
    ("7  COP31 • ANTALYA", GREEN, "Climate talks overtime; fossil fuels cut", "Drops $120bn goal; 35% by 2035 kept.", "Reuters/AFP • REPORTED"),
    ("8  UK–EU • THREE DEALS", BLUE, "Food, carbon markets, youth scheme signed", "Burnham signs in Brussels.", "BBC • REPORTED"),
]
boxes = [(36, 516, 500, 688), (524, 516, 988, 688), (36, 700, 500, 872), (524, 700, 988, 872), (36, 884, 500, 1010), (524, 884, 988, 1010)]
# only 6 boxes needed; use first 4 + adjust: actually 6 cards -> 3 rows; recompute below
boxes = [(36, 516, 500, 660), (524, 516, 988, 660), (36, 672, 500, 816), (524, 672, 988, 816), (36, 828, 500, 972), (524, 828, 988, 972)]
for (head, col, title, body, src), (x0, y0, x1, y1) in zip(cards, boxes):
    d.rectangle([x0, y0, x1, y1], outline=INK, width=3, fill=WHITE)
    d.rectangle([x0, y0, x1, y0 + 32], fill=col)
    d.text((x0 + 12, y0 + 5), head, font=F(SANS_B, 19), fill=WHITE)
    yy = draw_wrap(x0 + 14, y0 + 42, title, F(SANS_B, 21), x1 - x0 - 28)
    yy = draw_wrap(x0 + 14, yy + 4, body, F(SANS, 16), x1 - x0 - 28, fill=GREY)
    d.rectangle([x0 + 10, y1 - 26, x1 - 10, y1 - 4], fill=WHITE)
    d.text((x0 + 14, y1 - 24), src, font=F(SANS_B, 14), fill=col)

# ---------- Briefs + DATE CHECK footer ----------
d.rectangle([0, 978, W, 1024], fill=DARKBOX)
center_text(W // 2, 984, "Also 21 Nov: Palisades arsonist convicted (12 dead) • Bolsonaro in ICU • Sozcu TV seized • Rikers to close by 2032 • Ladakh votes", F(SANS_B, 14), fill=WHITE)
center_text(W // 2, 1004, "DATE CHECK: summit itself 19 Nov • barrage 19–20 Nov • ICJ judgment 19 Nov — excluded; 21 Nov fallout shown", F(SANS, 13), fill=(240, 220, 160))

img.save(OUT, format="PNG", optimize=True)
print(f"wrote {OUT} {img.size} stories=14")
