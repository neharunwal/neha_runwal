from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter


OUT_DIR = Path(__file__).resolve().parent / "assets"
OUT_DIR.mkdir(parents=True, exist_ok=True)

WIDTH = 1600
HEIGHT = 1100

image = Image.new("RGB", (WIDTH, HEIGHT), "#0b1020")
draw = ImageDraw.Draw(image)

# Soft layered gradients
for radius, color, position in [
    (420, (95, 225, 184), (200, 180)),
    (380, (141, 211, 255), (1180, 220)),
    (300, (125, 140, 255), (960, 760)),
    (250, (255, 165, 120), (360, 840)),
]:
    glow = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    x, y = position
    glow_draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color + (105,))
    glow = glow.filter(ImageFilter.GaussianBlur(70))
    image = Image.alpha_composite(image.convert("RGBA"), glow).convert("RGB")

draw = ImageDraw.Draw(image)

# Grid and connection lines
line_color = (173, 196, 229)
for x in range(120, WIDTH, 180):
    draw.line((x, 120, x, HEIGHT - 120), fill=line_color, width=1)
for y in range(120, HEIGHT, 160):
    draw.line((120, y, WIDTH - 120, y), fill=line_color, width=1)

nodes = [
    (280, 250), (520, 320), (760, 230), (1110, 310), (1340, 250),
    (360, 610), (690, 510), (980, 620), (1260, 560), (510, 820), (930, 850),
]

for start, end in zip(nodes, nodes[1:]):
    draw.line((start[0], start[1], end[0], end[1]), fill=(135, 225, 221), width=5)

for x, y in nodes:
    draw.ellipse((x - 16, y - 16, x + 16, y + 16), fill=(245, 250, 255))
    draw.ellipse((x - 34, y - 34, x + 34, y + 34), outline=(116, 242, 206), width=4)

# Card motifs
cards = [
    (180, 130, 520, 410),
    (890, 150, 1420, 470),
    (260, 620, 760, 980),
    (860, 640, 1410, 970),
]
for left, top, right, bottom in cards:
    draw.rounded_rectangle((left, top, right, bottom), radius=34, outline=(255, 255, 255), width=3, fill=(18, 29, 52))
    for offset in range(0, 4):
        line_y = top + 60 + offset * 46
        draw.rounded_rectangle((left + 42, line_y, right - 42, line_y + 18), radius=9, fill=(70 + offset * 20, 115 + offset * 16, 170 + offset * 14))

image = image.filter(ImageFilter.GaussianBlur(0.4))
image.save(OUT_DIR / "neha-hero.png", quality=95)
