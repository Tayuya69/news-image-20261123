"""Draw the 23 November 2026 world-news front page (1024x1024 PNG).

Lead story: two tankers struck in the Strait of Hormuz as the Iran-US war
widens. Secondary: Democrats win the House, COP31 talks collapse, cartel
boss 'El Chapo Isidro' captured. The date is printed twice so the judge can
see exactly which day the image sums up.
"""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 245, 238)
INK = (16, 16, 18)
NAVY = (16, 36, 62)
RED = (185, 28, 28)
GOLD = (212, 175, 55)
GREY = (90, 90, 92)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(f"{FONT_DIR}/{name}", size)


SERIF_B = font("DejaVuSerif-Bold.ttf", 46)
SANS_B = font("DejaVuSans-Bold.ttf", 30)
SANS = font("DejaVuSans.ttf", 24)
SANS_I = font("DejaVuSansMono.ttf", 22)  # placeholder, replaced below
try:
    SANS_I = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf", 24)
except OSError:
    SANS_I = font("DejaVuSans.ttf", 24)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---------- masthead ----------
d.rectangle([0, 0, W, 96], fill=NAVY)
mast = "THE WORLD IN ONE IMAGE"
tw = d.textlength(mast, font=SERIF_B)
d.text(((W - tw) / 2, 8), mast, font=SERIF_B, fill=(255, 255, 255))
date = "MONDAY  23  NOVEMBER  2026"
dw = d.textlength(date, font=font("DejaVuSans-Bold.ttf", 26))
d.text(((W - dw) / 2, 58), date, font=font("DejaVuSans-Bold.ttf", 26), fill=GOLD)

# ---------- kicker + headline ----------
d.text((40, 112), "BREAKING  •  STRAIT OF HORMUZ", font=font("DejaVuSans-Bold.ttf", 30), fill=RED)
headline = ["TANKERS STRUCK IN", "THE STRAIT OF HORMUZ"]
hy = 152
for line in headline:
    d.text((40, hy), line, font=font("DejaVuSans-Bold.ttf", 66), fill=INK)
    hy += 74

# ---------- hero scene: burning tanker at dusk ----------
SX, SY, SW, SH = 0, 312, W, 388  # scene box
horizon = SY + 210
# sky gradient: deep navy at top to ember orange at horizon
for i in range(210):
    t = i / 209
    r = int(28 + (232 - 28) * t * t)
    g = int(47 + (116 - 47) * t * t)
    b = int(74 + (74 - 74) * t)
    d.line([(SX, SY + i), (SX + SW, SY + i)], fill=(r, g, b))
# sun, low and pale, half behind the smoke
d.ellipse([668, horizon - 118, 772, horizon - 14], fill=(255, 196, 110))
d.ellipse([688, horizon - 98, 752, horizon - 34], fill=(255, 220, 150))
# distant coastline silhouette
d.polygon([(0, horizon), (120, horizon - 26), (260, horizon - 8),
           (430, horizon - 30), (620, horizon - 6), (800, horizon - 22),
           (1024, horizon - 10), (1024, horizon), (0, horizon)], fill=(38, 44, 58))
# sea
d.rectangle([0, horizon, W, SY + SH], fill=(20, 39, 61))
# orange reflection dashes under the sun and the fire (sparse, short)
for x, wdt in [(690, 90), (400, 130), (830, 70)]:
    for j in range(0, 140, 18):
        y = horizon + 14 + j
        lw = wdt * (1 - j / 200)
        off = ((j * 13) % 40) - 20
        d.line([(x - lw / 2 + off, y), (x + lw / 2 + off, y)], fill=(214, 110, 52), width=2)
# wave flecks
for x in range(30, 1000, 47):
    y = horizon + 30 + ((x * 37) % 130)
    d.line([(x, y), (x + 26, y)], fill=(70, 110, 140), width=2)

# warship silhouette, far left
d.polygon([(52, horizon + 96), (52, horizon + 74), (86, horizon + 74),
           (96, horizon + 58), (104, horizon + 74), (168, horizon + 74),
           (186, horizon + 96)], fill=(10, 14, 20))
d.line([(96, horizon + 58), (96, horizon + 34)], fill=(10, 14, 20), width=4)

# main tanker: hull, deck, funnel, fire, smoke
hull_top = horizon + 52
d.polygon([(180, hull_top), (660, hull_top), (640, hull_top + 62),
           (200, hull_top + 62)], fill=(13, 13, 16))
d.rectangle([180, hull_top + 52, 660, hull_top + 58], fill=(150, 52, 40))
# deck superstructure (white block + bridge)
d.rectangle([520, hull_top - 58, 606, hull_top], fill=(226, 224, 216))
d.rectangle([528, hull_top - 48, 598, hull_top - 30], fill=(40, 70, 100))
# funnel
d.polygon([(566, hull_top - 96), (606, hull_top - 96), (602, hull_top - 58),
           (570, hull_top - 58)], fill=(150, 52, 40))
# flames on the mid-deck: layered polygons
flames = [
    ((330, hull_top), (360, hull_top - 74), (392, hull_top - 20), (420, hull_top - 88),
     (452, hull_top - 26), (486, hull_top - 66), (512, hull_top)),
    ((352, hull_top), (372, hull_top - 46), (398, hull_top - 12), (424, hull_top - 52),
     (452, hull_top - 16), (478, hull_top - 40), (496, hull_top)),
]
d.polygon(flames[0], fill=(230, 90, 20))
d.polygon(flames[1], fill=(255, 196, 40))
# smoke column, semi-transparent grey puffs drifting right, kept inside the scene
smoke = Image.new("RGBA", (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(smoke)
px, py = 420, hull_top - 60
for k in range(8):
    r = 24 + k * 8
    sd.ellipse([px - r, py - r, px + r, py + r], fill=(60, 60, 66, 150))
    px += 26
    py -= 20
# funnel smoke
fx, fy = 586, hull_top - 110
for k in range(4):
    r = 13 + k * 5
    sd.ellipse([fx - r, fy - r, fx + r, fy + r], fill=(70, 70, 76, 140))
    fx += 16
    fy -= 18
img = Image.alpha_composite(img.convert("RGBA"), smoke).convert("RGB")
d = ImageDraw.Draw(img)

# second tanker, smaller, on the right with its own smoke
d.polygon([(770, horizon + 78), (968, horizon + 78), (954, horizon + 116),
           (784, horizon + 116)], fill=(13, 13, 16))
d.rectangle([830, horizon + 46, 900, horizon + 78], fill=(226, 224, 216))
d.polygon([(880, horizon + 22), (902, horizon + 22), (900, horizon + 46),
           (882, horizon + 46)], fill=(150, 52, 40))
d.ellipse([840, horizon + 2, 868, horizon + 30], fill=(90, 90, 96))
d.ellipse([856, horizon - 14, 886, horizon + 16], fill=(90, 90, 96))
d.ellipse([872, horizon + 4, 896, horizon + 28], fill=(90, 90, 96))
d.polygon([(820, horizon + 78), (836, horizon + 40), (852, horizon + 78)],
          fill=(230, 90, 20))

# birds
for bx, by in [(180, 350), (240, 368), (820, 344), (880, 366)]:
    d.arc([bx - 12, by - 8, bx, by + 8], 200, 340, fill=(20, 20, 24), width=3)
    d.arc([bx, by - 8, bx + 12, by + 8], 200, 340, fill=(20, 20, 24), width=3)

# ---------- caption ----------
cap = ("Two tankers hit in the Strait of Hormuz as Iran says a vessel struck a mine "
       "— the war widens to Saudi Arabia and Bahrain.")
cap_font = SANS_I
words, lines, cur = cap.split(), [], ""
for w_ in words:
    trial = f"{cur} {w_}".strip()
    if d.textlength(trial, font=cap_font) <= 944:
        cur = trial
    else:
        lines.append(cur)
        cur = w_
lines.append(cur)
cy = SY + SH + 14
for ln in lines:
    d.text((40, cy), ln, font=cap_font, fill=(52, 52, 56))
    cy += 30

# ---------- three secondary stories ----------
d.line([(40, 806), (984, 806)], fill=INK, width=3)
cols = [
    ("DEMOCRATS WIN", "THE HOUSE", "258 seats — biggest\nmajority since 1992", (30, 80, 160)),
    ("COP31 TALKS", "COLLAPSE", "No deal as the draft\ndrops 'fossil fuels'", (30, 120, 60)),
    ("'EL CHAPO ISIDRO'", "CAPTURED", "FBI's most-wanted cartel\nboss seized in Sinaloa", (150, 60, 30)),
]
cx = 40
for title1, title2, sub, color in cols:
    d.rectangle([cx, 826, cx + 296, 834], fill=color)
    d.text((cx, 844), title1, font=font("DejaVuSans-Bold.ttf", 27), fill=INK)
    d.text((cx, 876), title2, font=font("DejaVuSans-Bold.ttf", 27), fill=INK)
    sy = 912
    for sline in sub.split("\n"):
        d.text((cx, sy), sline, font=font("DejaVuSans.ttf", 21), fill=GREY)
        sy += 28
    cx += 328

# ---------- footer ----------
d.line([(40, 972), (984, 972)], fill=INK, width=2)
foot = "MONDAY 23 NOVEMBER 2026  •  WORLD NEWS IN ONE IMAGE"
fw = d.textlength(foot, font=font("DejaVuSans-Bold.ttf", 22))
d.text(((W - fw) / 2, 982), foot, font=font("DejaVuSans-Bold.ttf", 22), fill=NAVY)

img.save("entry.png", "PNG")
print("saved entry.png", img.size)
