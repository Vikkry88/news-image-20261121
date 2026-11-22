#!/usr/bin/env python3
"""Dense front-page image: world news of Saturday 21 November 2026 (v2).

42 stories, 7 regions, world map with pins, UTC timeline, day-in-numbers,
source + confidence on every story, DATE CHECK box. Shapes/text only (PIL).
Writes entry.png beside this file (1024x1024 PNG, deterministic).
"""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

PAPER = (252, 250, 244)
INK = (24, 24, 30)
RED = (178, 30, 30)
BLUE = (24, 62, 138)
TEAL = (12, 110, 110)
GREEN = (26, 120, 62)
ORANGE = (196, 100, 16)
PURPLE = (96, 44, 140)
GREY = (96, 96, 104)
LIGHT = (240, 236, 224)
DARK = (32, 36, 50)
GOLD = (255, 214, 90)
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


def draw_wrap(x, y, text, font, maxw, fill=INK, leading=2, max_lines=99):
    lines = wrap(text, font, maxw)[:max_lines]
    lh = font.size + leading
    for ln in lines:
        d.text((x, y), ln, font=font, fill=fill)
        y += lh
    return y


def center(cx, y, text, font, fill=INK):
    w = d.textlength(text, font=font)
    d.text((cx - w / 2, y), text, font=font, fill=fill)
    return y + font.size


def pin(cx, cy, n, col=RED):
    d.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill=col, outline=WHITE, width=1)
    t = str(n)
    f = F(SANS_B, 9 if n < 10 else 7)
    w = d.textlength(t, font=f)
    d.text((cx - w / 2, cy - f.size / 2 - 1), t, font=f, fill=WHITE)


def tag(x, y, text, col):
    f = F(SANS_B, 9)
    w = d.textlength(text, font=f) + 8
    d.rectangle([x, y, x + w, y + 14], fill=col)
    d.text((x + 4, y + 2), text, font=f, fill=WHITE)
    return x + w + 4


# ---------- Masthead ----------
d.rectangle([0, 0, W, 86], fill=DARK)
center(W // 2, 6, "THE WORLD TODAY", F(SERIF_B, 44), fill=WHITE)
center(W // 2, 56, "Saturday 21 November 2026  •  42 stories  •  7 regions  •  World news in one picture", F(SANS_B, 15), fill=GOLD)
d.rectangle([0, 86, W, 92], fill=RED)
# how-to-read strip
d.rectangle([0, 92, W, 112], fill=LIGHT)
center(W // 2, 96, "HOW TO READ: pins match story numbers  •  source + REPORTED / FORECAST / CLAIM / DISPUTED on every story  •  DATE CHECK at foot", F(SANS_B, 11), fill=INK)

# ---------- UTC timeline ----------
d.rectangle([0, 112, W, 164], fill=WHITE, outline=INK, width=1)
d.text((10, 116), "21 NOV — UTC TIMELINE (first-reported times)", font=F(SANS_B, 12), fill=RED)
tl = [("03:34", "OFAC list"), ("07:15", "Haiti death"), ("09:26", "Basra fire"), ("11:27", "Hormuz hits"),
      ("13:14", "EU budget"), ("15:11", "EU–Indonesia"), ("18:17", "Finland probe"), ("23:25", "Bahrain fire")]
d.line([16, 140, 1008, 140], fill=GREY, width=2)
for i, (t, lab) in enumerate(tl):
    xx = 10 + i * 126
    d.ellipse([xx + 8, 136, xx + 16, 144], fill=RED)
    d.text((xx, 146), t, font=F(SANS_B, 10), fill=INK)
    d.text((xx, 157), lab, font=F(SANS, 8), fill=GREY)

# ---------- Day in numbers ----------
d.rectangle([0, 164, W, 200], fill=BLUE)
center(W // 2, 168, "DAY IN NUMBERS", F(SANS_B, 13), fill=GOLD)
nums = "9–6 ICJ vote  •  275 drones CLAIM  •  €1bn EU aid  •  M6.7 Peru  •  S&P −3.7% → 6,910  •  Nikkei −5.06%"
center(W // 2, 182, nums, F(SANS_B, 12), fill=WHITE)
nums2 = "Gold $3,515 −4.62%  •  Brent ~$90  •  4.1 km incursion  •  6,800 buildings  •  35% by 2035  •  $120bn dropped"
center(W // 2, 192, nums2, F(SANS_B, 10), fill=(200, 220, 255))

# ---------- 3 lead stories ----------
leads = [
    ("1  SHENZHEN FALLOUT", RED,
     "Trump defends calling Putin 'friend'; Zelensky: 'killer'",
     "After 19 Nov summit: nuclear-risk talks agreed. No Ukraine deal; Europe left out.",
     "BBC / CBS • REPORTED"),
    ("2  UKRAINE WAR WIDENS", ORANGE,
     "Kryvyi Rih hit; ship burns off Finland; EU sends €1bn",
     "Strike kills 2 in Zelensky's hometown. Ship burns after Sat drone hit.",
     "Reuters / BBC • REPORTED + CLAIM"),
    ("3  COP31 OVERTIME — ANTALYA", GREEN,
     "Fossil fuels cut from draft; $120bn dropped",
     "Past Friday close: 35% electricity by 2035 kept. France & Panama push back.",
     "Reuters / AFP • REPORTED"),
]
lx = [8, 348, 688]
for i, (head, col, title, body, src) in enumerate(leads):
    x0, x1 = lx[i], lx[i] + 328
    d.rectangle([x0, 202, x1, 372], outline=INK, width=2, fill=WHITE)
    d.rectangle([x0, 202, x1, 228], fill=col)
    center((x0 + x1) // 2, 207, head, F(SANS_B, 15), fill=WHITE)
    # simple illustration strip
    iy = 232
    if i == 0:
        for cx, c, lab in [(x0 + 70, (200, 40, 40), "USA"), (x0 + 164, (210, 30, 30), "CHINA"), (x0 + 258, (40, 80, 180), "RUSSIA")]:
            d.ellipse([cx - 16, iy, cx + 16, iy + 32], fill=(240, 210, 170), outline=INK, width=2)
            d.rectangle([cx - 20, iy + 32, cx + 20, iy + 52], fill=c, outline=INK, width=2)
            center(cx, iy + 37, lab, F(SANS_B, 10), fill=WHITE)
        center((x0 + x1) // 2, iy + 56, "'friend'  vs  'killer'", F(SANS_B, 12), fill=RED)
    elif i == 1:
        d.rectangle([x0 + 8, iy, x1 - 8, iy + 58], fill=(70, 60, 90))
        for bx, bh in [(x0 + 30, 36), (x0 + 90, 48), (x0 + 150, 32), (x0 + 210, 44), (x0 + 265, 34)]:
            d.rectangle([bx, iy + 58 - bh, bx + 34, iy + 58], fill=(30, 30, 40))
        for mx, my in [(x0 + 60, iy + 6), (x0 + 170, iy + 3), (x0 + 250, iy + 7)]:
            d.line([mx, my, mx + 24, my + 26], fill=(255, 170, 60), width=4)
            d.ellipse([mx + 20, my + 22, mx + 30, my + 32], fill=(255, 90, 40))
        center((x0 + x1) // 2, iy + 62, "275 drones CLAIM  •  €1bn EU aid", F(SANS_B, 11), fill=ORANGE)
    else:
        d.rectangle([x0 + 8, iy, x1 - 8, iy + 58], fill=(210, 235, 220))
        d.ellipse([x0 + 138, iy + 6, x0 + 190, iy + 52], fill=(90, 180, 110), outline=INK, width=2)
        d.text((x0 + 144, iy + 20), "1.5°C", font=F(SANS_B, 15), fill=WHITE)
        d.line([x0 + 30, iy + 48, x0 + 110, iy + 48], fill=RED, width=5)
        d.text((x0 + 30, iy + 28), "fossil fuels ✗", font=F(SANS_B, 12), fill=RED)
        d.text((x0 + 214, iy + 28), "35% by 2035", font=F(SANS_B, 12), fill=GREEN)
        center((x0 + x1) // 2, iy + 62, "nearly 200 countries • no deal yet", F(SANS_B, 11), fill=GREEN)
    y = draw_wrap(x0 + 10, 308, title, F(SANS_B, 14), 308, fill=INK, leading=1, max_lines=2)
    y = draw_wrap(x0 + 10, y + 1, body, F(SANS, 10), 308, fill=(60, 60, 66), leading=1, max_lines=2)
    d.rectangle([x0 + 8, 356, x1 - 8, 370], fill=WHITE)
    d.text((x0 + 10, 358), src, font=F(SANS_B, 10), fill=col)

# ---------- Map (left) + picture cards (right) ----------
d.rectangle([8, 378, 400, 648], outline=INK, width=2, fill=(214, 232, 245))
d.rectangle([8, 378, 400, 402], fill=BLUE)
center(204, 383, "WORLD MAP — pins = story numbers", F(SANS_B, 13), fill=WHITE)
# crude continents (blobs)
conts = [
    ([(30, 450), (90, 425), (150, 435), (140, 500), (95, 540), (55, 520)], (140, 190, 130)),   # N America
    ([(110, 560), (150, 555), (165, 610), (135, 640), (115, 600)], (150, 200, 140)),          # S America
    ([(195, 430), (245, 425), (250, 465), (210, 480), (195, 455)], (170, 200, 150)),          # Europe
    ([(205, 485), (260, 480), (270, 545), (230, 575), (205, 535)], (220, 200, 130)),          # Africa
    ([(255, 430), (360, 420), (380, 480), (320, 510), (265, 480)], (180, 205, 155)),          # Asia
    ([(320, 545), (375, 540), (385, 580), (340, 595), (320, 570)], (200, 215, 160)),          # Oceania
]
for pts, col in conts:
    d.polygon(pts, fill=col, outline=INK)
pinpos = {
    1: (338, 458), 2: (238, 446), 3: (254, 474), 4: (312, 488), 5: (274, 492), 6: (132, 588),
    7: (220, 438), 8: (230, 454), 9: (50, 480), 10: (144, 600), 11: (252, 464), 12: (86, 460),
    13: (76, 474), 14: (246, 434), 15: (300, 466), 16: (68, 450), 17: (64, 468), 18: (76, 456),
    19: (90, 466), 20: (120, 526), 21: (96, 506), 22: (140, 620), 23: (234, 430), 24: (242, 428),
    25: (218, 450), 26: (228, 442), 27: (212, 460), 28: (226, 440), 29: (280, 502), 30: (272, 480),
    31: (268, 476), 32: (264, 510), 33: (260, 486), 34: (220, 530), 35: (240, 564), 36: (350, 450),
    37: (344, 462), 38: (304, 480), 39: (320, 524), 40: (306, 488), 41: (266, 498), 42: (238, 422),
}
for n, (px, py) in pinpos.items():
    pin(px, py, n)
d.text((14, 626), "42 pins • leads 1–3 • cards 4–15 • briefs 16–42", font=F(SANS_B, 11), fill=INK)

cards = [
    ("4 ICJ • MYANMAR", BLUE, "Rejects 9–6 genocide ruling as 'biased'", "Judgment 19 Nov; rejection 21 Nov.", "Reuters • REPORTED"),
    ("5 HORMUZ", TEAL, "2 tankers hit off Khasab; mine claim", "UKMTO 215/216. No casualties.", "UKMTO • DISPUTED"),
    ("6 PERU QUAKE", ORANGE, "M6.7 Junín, felt in Lima", "No deaths or damage reported.", "USGS • REPORTED"),
    ("7 UK–EU DEALS", BLUE, "3 deals: food, carbon, youth scheme", "Burnham signs in Brussels.", "BBC • REPORTED"),
    ("8 AI WEAPONS", PURPLE, "~100 back binding rules by 2028", "US, Russia, Israel oppose.", "NPR • REPORTED"),
    ("9 PALISADES FIRE", RED, "Arsonist convicted; 12 dead", "6,800+ buildings destroyed.", "AP • REPORTED"),
    ("10 BRAZIL", GREEN, "Bolsonaro in ICU, stable", "Bowel obstruction; surgery weighed.", "Al Jazeera • REPORTED"),
    ("11 TURKEY TV", RED, "State seizes Sozcu TV", "Last independent channel falls.", "RFI • REPORTED"),
    ("12 NEW YORK", BLUE, "Rikers Island to close by 2032", "Mayor Mamdani announces plan.", "BBC • FORECAST"),
    ("13 MARKETS", ORANGE, "AI selloff: S&P −3.7% to 6,910", "Tech worst week since 2020.", "CNBC • REPORTED"),
    ("14 ESTONIA", BLUE, "Shuts Russia crossings Dec 1", "Queues form across border.", "Straits Times • FORECAST"),
    ("15 LADAKH VOTE", TEAL, "First elections since 2019", "Leh & Kargil vote; ends Nov 30.", "The Hindu • REPORTED"),
]
cx0 = 408
for i, (head, col, title, body, src) in enumerate(cards):
    col_i = i % 3
    row_i = i // 3
    x0 = cx0 + col_i * 204
    y0 = 378 + row_i * 68
    x1, y1 = x0 + 198, y0 + 64
    d.rectangle([x0, y0, x1, y1], outline=INK, width=1, fill=WHITE)
    d.rectangle([x0, y0, x1, y0 + 17], fill=col)
    d.text((x0 + 5, y0 + 3), head, font=F(SANS_B, 10), fill=WHITE)
    y = draw_wrap(x0 + 5, y0 + 20, title, F(SANS_B, 11), 188, fill=INK, leading=1, max_lines=2)
    draw_wrap(x0 + 5, y, body, F(SANS, 9), 188, fill=GREY, leading=1, max_lines=1)
    d.rectangle([x0 + 4, y1 - 13, x1 - 4, y1 - 1], fill=WHITE)
    d.text((x0 + 5, y1 - 12), src, font=F(SANS_B, 8), fill=col)

# ---------- Briefs by region (3 columns) ----------
d.rectangle([8, 654, 1016, 672], fill=DARK)
center(512, 658, "MORE OF 21 NOVEMBER — one-line briefs by region (16–42)", F(SANS_B, 13), fill=GOLD)

regions = [
    ("NORTH AMERICA", RED, [
        ("16", "FBI probes apparent hack of criminal database.", "REPORTED"),
        ("17", "US teen pleads not guilty in Hindu-temple plot nr Chicago.", "AP • REPORTED"),
        ("18", "Trump adviser Miller 'earned $15M in a year' — report.", "CLAIM"),
        ("19", "Lock of George Washington's hair sells for $4,000.", "REPORTED"),
    ]),
    ("LATIN AMERICA", GREEN, [
        ("20", "Haiti: Salvadoran soldier dies after blast (3 total).", "REPORTED"),
        ("21", "Mexico: 'Chapo Isidro' arrested 20 Nov; unrest 21 Nov.", "BBC • REPORTED"),
        ("22", "Argentina approves large LNG project.", "REPORTED"),
    ]),
    ("EUROPE", BLUE, [
        ("23", "Denmark: Russia plot to kill rapper; Moscow denies.", "DISPUTED"),
        ("24", "Finland probes Russian helicopter 4.1 km incursion.", "REPORTED"),
        ("25", "French police sentenced over Zecler beating.", "AFP • REPORTED"),
        ("26", "Costa proposes €1.78tn EU budget 2028–34.", "REPORTED"),
        ("27", "Spain heads to Nov 29 election.", "El País • FORECAST"),
        ("28", "Brussels: flight cancellations expected.", "FORECAST"),
    ]),
    ("MIDDLE EAST & GULF", ORANGE, [
        ("29", "Bahrain blames Iran for industrial fire; UAE condemns.", "CLAIM"),
        ("30", "Basra Hartha fire: 4 dead, 35 injured.", "REPORTED"),
        ("31", "Iraq–Kata'ib Hezbollah joint ops centre agreed.", "REPORTED"),
        ("32", "Saudi–Houthi trade port-strike threats.", "CLAIM"),
        ("33", "Gaza Jabalia death (WAFA); W. Bank guard kills 1.", "REPORTED"),
    ]),
    ("AFRICA", TEAL, [
        ("34", "Nigeria boat capsize: NEMA reports 24 bodies.", "REPORTED"),
        ("35", "S. Africa ANC fights to hold key cities.", "REPORTED"),
    ]),
    ("ASIA-PACIFIC", PURPLE, [
        ("36", "Japan sidelined at Shenzhen; Takaichi cool welcome.", "Japan Times • REPORTED"),
        ("37", "S. Korea ruling party moves to impeach chief justice.", "Yonhap • FORECAST"),
        ("38", "Nepal PM Shah: first India trip Nov 22–23.", "BBC • FORECAST"),
        ("39", "EU–Indonesia CEPA & IPA signed.", "Commission • REPORTED"),
        ("40", "Sensex +2.3% bucks global selloff.", "REPORTED"),
    ]),
    ("GLOBAL", INK, [
        ("41", "UN: Yemen displaced +357,000 since last August.", "REPORTED"),
        ("42", "Trafalgar Square Christmas tree felled in Norway.", "REPORTED"),
    ]),
]
# layout: col A = NA+LatAm+Global, col B = Europe+Africa, col C = ME+AsiaPac
cols = [
    [regions[0], regions[1], regions[6]],
    [regions[2], regions[4]],
    [regions[3], regions[5]],
]
colx = [8, 348, 688]
for ci, groups in enumerate(cols):
    x0 = colx[ci]
    y = 676
    for rname, rcol, items in groups:
        d.rectangle([x0, y, x0 + 328, y + 16], fill=rcol)
        d.text((x0 + 6, y + 2), rname, font=F(SANS_B, 11), fill=WHITE)
        y += 18
        for num, text, src in items:
            d.ellipse([x0 + 2, y, x0 + 20, y + 18], fill=rcol)
            f = F(SANS_B, 10)
            w = d.textlength(num, font=f)
            d.text((x0 + 11 - w / 2, y + 3), num, font=f, fill=WHITE)
            y2 = draw_wrap(x0 + 24, y, text, F(SANS, 11), 304, fill=INK, leading=1, max_lines=2)
            d.text((x0 + 24, y2), src, font=F(SANS_B, 8), fill=GREY)
            y = y2 + 11
        y += 3

# ---------- DATE CHECK + footer ----------
d.rectangle([8, 946, 1016, 994], outline=RED, width=2, fill=(255, 244, 230))
d.text((14, 950), "DATE CHECK — excluded as other days' news (not counted in the 42):", font=F(SANS_B, 12), fill=RED)
draw_wrap(14, 966,
          "Shenzhen summit itself 19 Nov • 110-missile barrage night 19–20 Nov • ICJ judgment delivered 19 Nov (21 Nov = rejection) • EU €1bn Council decision 20 Nov 15:50 (21 Nov = coverage) • 'Chapo Isidro' arrested 20 Nov • OFAC 4 Iranians published 20 Nov • COP31 collapse & S. Korea minister resignation 22 Nov",
          F(SANS, 11), 996, fill=INK, leading=2, max_lines=2)
center(512, 998, "Sources as tagged on each story  •  Sat 21 Nov 2026 only  •  v3 — 42 stories, 7 regions, map + UTC timeline + day in numbers", F(SANS_B, 11), fill=GREY)

img.save(OUT, format="PNG", optimize=True)
print(f"wrote {OUT} {img.size} stories=42")
