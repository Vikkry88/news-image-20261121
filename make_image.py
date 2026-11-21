#!/usr/bin/env python3
"""Draw a newspaper front-page image summing up world news of Saturday 21 November 2026.

Shapes and text only (PIL). No photos, no network. Deterministic output.
Writes entry.png beside this file (1024x1024 PNG).
"""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

PAPER = (250, 246, 236)
INK = (28, 28, 32)
RED = (176, 32, 32)
BLUE = (30, 70, 140)
GOLD = (176, 128, 20)
GREY = (110, 110, 115)
LIGHT = (238, 231, 214)
SKY = (198, 220, 240)
DARKBOX = (40, 44, 58)

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
d.rectangle([0, 0, W, 148], fill=DARKBOX)
center_text(W // 2, 14, "THE WORLD TODAY", F(SERIF_B, 62), fill=(255, 255, 255))
center_text(W // 2, 86, "Saturday 21 November 2026  •  World News in One Picture", F(SANS_B, 24), fill=(240, 220, 160))
d.rectangle([0, 148, W, 156], fill=RED)

# ---------- Lead story ----------
d.rectangle([24, 172, 1000, 178], fill=INK)
center_text(W // 2, 186, "PEACE TALKS BY DAY, MISSILES BY NIGHT", F(SERIF_B, 40), fill=RED)
y = draw_wrap(60, 236, "Trump, Xi and Putin hold first-ever three-way summit in Shenzhen — "
                      "hours later Russia fires 110+ missiles and 400+ drones at Ukraine",
              F(SANS_B, 25), 904)
# two lead panels
# left: summit table
d.rectangle([36, 322, 500, 540], outline=INK, width=3, fill=SKY)
d.rectangle([36, 322, 500, 356], fill=BLUE)
center_text(268, 328, "SHENZHEN SUMMIT", F(SANS_B, 22), fill=(255, 255, 255))
# table
d.ellipse([120, 430, 420, 500], fill=(120, 84, 48), outline=INK, width=3)
# three leaders: simple figures with flag colours
for cx, col, label in [(150, (200, 40, 40), "USA"), (268, (210, 30, 30), "CHINA"), (386, (40, 80, 180), "RUSSIA")]:
    d.ellipse([cx - 26, 368, cx + 26, 420], fill=(240, 210, 170), outline=INK, width=2)
    d.rectangle([cx - 30, 420, cx + 30, 462], fill=col, outline=INK, width=2)
    center_text(cx, 468, label, F(SANS_B, 18), fill=(255, 255, 255))
d.rectangle([36, 498, 500, 540], fill=(255, 255, 255))
draw_wrap(52, 504, "Trump calls Putin 'my friend'; 'very good talks' — no breakthrough", F(SANS, 16), 432)
# right: barrage
d.rectangle([524, 322, 988, 540], outline=INK, width=3, fill=(60, 50, 70))
d.rectangle([524, 322, 988, 356], fill=RED)
center_text(756, 328, "KYIV UNDER FIRE", F(SANS_B, 22), fill=(255, 255, 255))
# skyline
for bx, bh in [(545, 90), (600, 130), (660, 100), (720, 150), (790, 110), (850, 140), (910, 95)]:
    d.rectangle([bx, 510 - bh, bx + 46, 510], fill=(30, 30, 40), outline=(0, 0, 0), width=1)
    for wy in range(510 - bh + 10, 500, 22):
        d.rectangle([bx + 8, wy, bx + 16, wy + 8], fill=(255, 220, 120))
        d.rectangle([bx + 26, wy, bx + 34, wy + 8], fill=(255, 220, 120))
# missiles
for mx, my in [(580, 380), (680, 365), (800, 385), (900, 370)]:
    d.line([mx, my, mx + 46, my + 52], fill=(255, 160, 60), width=5)
    d.ellipse([mx + 40, my + 46, mx + 56, my + 62], fill=(255, 90, 40))
    d.polygon([(mx - 4, my - 4), (mx + 10, my - 2), (mx + 2, my + 12)], fill=(220, 220, 220))
d.rectangle([524, 498, 988, 540], fill=(255, 255, 255))
draw_wrap(540, 504, "Bridges hit, power plants targeted; missiles reported over Poland (NATO)", F(SANS, 16), 432, fill=INK)

# ---------- Lower grid: 4 stories ----------
d.rectangle([24, 556, 1000, 562], fill=INK)
boxes = [
    (36, 576, 500, 792),
    (524, 576, 988, 792),
    (36, 808, 500, 990),
    (524, 808, 988, 990),
]

# Story 1: ICJ Myanmar
x0, y0, x1, y1 = boxes[0]
d.rectangle([x0, y0, x1, y1], outline=INK, width=3, fill=(255, 255, 255))
d.rectangle([x0, y0, x1, y0 + 32], fill=BLUE)
d.text((x0 + 12, y0 + 5), "WORLD COURT  •  MYANMAR", font=F(SANS_B, 20), fill=(255, 255, 255))
# courthouse icon
cx = x0 + 70
d.polygon([(cx - 44, y0 + 78), (cx + 44, y0 + 78), (cx, y0 + 48)], fill=GOLD, outline=INK)
for i in range(4):
    px = cx - 36 + i * 24
    d.rectangle([px, y0 + 82, px + 12, y0 + 128], fill=(220, 220, 220), outline=INK)
d.rectangle([cx - 46, y0 + 128, cx + 46, y0 + 138], fill=GOLD, outline=INK)
_y = draw_wrap(x0 + 128, y0 + 44, "Court rules Myanmar committed genocide against the Rohingya", F(SANS_B, 23), x1 - x0 - 142)
draw_wrap(x0 + 128, _y + 4, "Judges vote 9–6; state held responsible for crimes in Rakhine.", F(SANS, 17), x1 - x0 - 142, fill=GREY)

# Story 2: Peru quake
x0, y0, x1, y1 = boxes[1]
d.rectangle([x0, y0, x1, y1], outline=INK, width=3, fill=(255, 255, 255))
d.rectangle([x0, y0, x1, y0 + 32], fill=(150, 90, 20))
d.text((x0 + 12, y0 + 5), "PERU  •  EARTHQUAKE", font=F(SANS_B, 20), fill=(255, 255, 255))
# mountains + crack + rings
mx = x0 + 70
d.polygon([(mx - 50, y0 + 140), (mx - 10, y0 + 70), (mx + 20, y0 + 110), (mx + 52, y0 + 140)], fill=(140, 110, 80), outline=INK)
d.line([mx - 8, y0 + 108, mx + 2, y0 + 122, mx - 6, y0 + 138], fill=RED, width=4)
for r in (18, 30, 42):
    d.ellipse([mx + 30 - r, y0 + 60 - r // 2, mx + 30 + r, y0 + 60 + r // 2], outline=RED, width=2)
center_text(mx, y0 + 146, "M 6.7", F(SANS_B, 24), fill=RED)
_y = draw_wrap(x0 + 128, y0 + 44, "Magnitude 6.7 quake shakes Peru's Andes, felt in Lima", F(SANS_B, 23), x1 - x0 - 142)
draw_wrap(x0 + 128, _y + 4, "Deep tremor near Junín; people flee homes. No deaths or major damage reported.", F(SANS, 17), x1 - x0 - 142, fill=GREY)

# Story 3: EU/UK aid to Ukraine
x0, y0, x1, y1 = boxes[2]
d.rectangle([x0, y0, x1, y1], outline=INK, width=3, fill=(255, 255, 255))
d.rectangle([x0, y0, x1, y0 + 32], fill=(30, 110, 60))
d.text((x0 + 12, y0 + 5), "EUROPE  •  AID FOR UKRAINE", font=F(SANS_B, 20), fill=(255, 255, 255))
# drone icon
cx, cy = x0 + 70, y0 + 92
d.rectangle([cx - 16, cy - 10, cx + 16, cy + 10], fill=INK)
for dx, dy in [(-38, -22), (38, -22), (-38, 22), (38, 22)]:
    d.line([cx, cy, cx + dx, cy + dy], fill=INK, width=3)
    d.ellipse([cx + dx - 12, cy + dy - 5, cx + dx + 12, cy + dy + 5], outline=INK, width=2)
center_text(cx, y0 + 142, "drones", F(SANS_B, 18), fill=INK)
_y = draw_wrap(x0 + 128, y0 + 44, "EU approves €1 billion in military aid; UK pledges 1,000+ drones", F(SANS_B, 23), x1 - x0 - 142)
draw_wrap(x0 + 128, _y + 4, "Joint weapons purchases for Kyiv; deliveries planned through 2027.", F(SANS, 17), x1 - x0 - 142, fill=GREY)

# Story 4: Hormuz tanker
x0, y0, x1, y1 = boxes[3]
d.rectangle([x0, y0, x1, y1], outline=INK, width=3, fill=(255, 255, 255))
d.rectangle([x0, y0, x1, y0 + 32], fill=(20, 90, 120))
d.text((x0 + 12, y0 + 5), "STRAIT OF HORMUZ  •  TANKER", font=F(SANS_B, 20), fill=(255, 255, 255))
# tanker icon
cx, cy = x0 + 70, y0 + 100
d.polygon([(cx - 52, cy), (cx + 52, cy), (cx + 38, cy + 26), (cx - 38, cy + 26)], fill=(60, 60, 70), outline=INK)
d.rectangle([cx - 40, cy - 16, cx + 20, cy], fill=(200, 60, 40), outline=INK)
d.rectangle([cx + 24, cy - 26, cx + 40, cy], fill=(220, 220, 220), outline=INK)
# flame
d.polygon([(cx - 20, cy - 16), (cx - 8, cy - 44), (cx + 2, cy - 16)], fill=(255, 120, 30))
d.polygon([(cx - 14, cy - 16), (cx - 8, cy - 32), (cx - 2, cy - 16)], fill=(255, 200, 60))
for i in range(3):
    d.arc([cx - 50 + i * 34, cy + 30, cx - 18 + i * 34, cy + 46], 0, 180, fill=BLUE, width=3)
_y = draw_wrap(x0 + 128, y0 + 44, "Tanker struck and set on fire near Strait of Hormuz", F(SANS_B, 23), x1 - x0 - 142)
draw_wrap(x0 + 128, _y + 4, "Maritime warning issued off Oman; shipping on alert in key oil route.", F(SANS, 17), x1 - x0 - 142, fill=GREY)

# ---------- Footer ----------
center_text(W // 2, 1000 - 6, "Also today: US sanctions four Iranians over oil revenues  •  EU–UK youth mobility deal  •  India shares see record foreign inflow", F(SANS, 15), fill=GREY)

img.save(OUT, format="PNG", optimize=True)
print(f"wrote {OUT} {img.size}")
