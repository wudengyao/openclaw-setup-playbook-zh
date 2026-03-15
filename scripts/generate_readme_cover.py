from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

W, H = 1600, 560
img = Image.new("RGB", (W, H), "#0b0c10")
d = ImageDraw.Draw(img)

# background blocks
for i in range(0, H, 4):
    c = 11 + (i % 24)
    d.line((0, i, W, i), fill=(c, c, c + 6), width=1)

# left panel
d.rounded_rectangle((80, 70, 560, 490), radius=70, fill="#1a1020", outline="#36263f", width=3)

# simple lobster icon
cx, cy = 320, 280
d.ellipse((cx - 95, cy - 105, cx + 95, cy + 105), fill="#ff4f57")
d.ellipse((cx - 70, cy - 175, cx + 70, cy - 55), fill="#ff6167")
d.ellipse((cx - 42, cy - 126, cx - 18, cy - 102), fill="#121826")
d.ellipse((cx + 18, cy - 126, cx + 42, cy - 102), fill="#121826")
d.ellipse((cx - 36, cy - 120, cx - 28, cy - 112), fill="#4affdf")
d.ellipse((cx + 24, cy - 120, cx + 32, cy - 112), fill="#4affdf")
d.line((cx - 20, cy - 176, cx - 62, cy - 202), fill="#ff8a8f", width=6)
d.line((cx + 20, cy - 176, cx + 62, cy - 202), fill="#ff8a8f", width=6)
d.ellipse((cx - 145, cy - 66, cx - 78, cy + 2), fill="#f14952")
d.ellipse((cx + 78, cy - 66, cx + 145, cy + 2), fill="#f14952")
d.rectangle((cx - 40, cy + 90, cx - 14, cy + 136), fill="#df3f48")
d.rectangle((cx + 14, cy + 90, cx + 40, cy + 136), fill="#df3f48")

# fonts
font_candidates = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
]

def pick_font(size):
    for p in font_candidates:
        fp = Path(p)
        if fp.exists():
            return ImageFont.truetype(str(fp), size)
    return ImageFont.load_default()

f1 = pick_font(76)
f2 = pick_font(58)
f3 = pick_font(34)
f4 = pick_font(27)

x = 650
d.text((x, 108), "OpenClaw", font=f1, fill="#ff5a64")
d.text((x + 408, 112), "🦞", font=f3, fill="#ff7f50")

# strike-through old names
for y, txt in [(170, "Moltbot"), (220, "Clawdbot")]:
    d.text((x + 6, y), txt, font=f3, fill="#ff7179")
    tw = d.textlength(txt, font=f3)
    d.line((x + 2, y + 20, x + tw + 20, y + 6), fill="#f2f4f8", width=7)

d.text((x, 278), "Skills Collection", font=f2, fill="#f7f8fb")
d.text((x, 350), "社区技能全量快照 · 分类索引 · 一键检索", font=f3, fill="#ccd1db")

# badges
badges = [
    ("awesome", "#45355e", "#ffffff"),
    ("AI Agent Engineering", "#123943", "#85ffe6"),
    ("skills 5400+", "#15679f", "#e9f4ff"),
    ("updated 2026-03-15", "#2f8642", "#eaffef"),
]

bx, by = x, 410
for text, bg, fg in badges:
    bw = int(d.textlength(text, font=f4) + 34)
    d.rounded_rectangle((bx, by, bx + bw, by + 44), radius=10, fill=bg)
    d.text((bx + 16, by + 8), text, font=f4, fill=fg)
    bx += bw + 12

# brand
d.text((1260, 490), "voltagent inspired", font=pick_font(36), fill="#19ddb1")

# border
d.rounded_rectangle((18, 18, W - 18, H - 18), radius=16, outline="#252831", width=2)

out_dir = Path("/Users/wudengyao/openclaw-setup-playbook-zh/assets")
out_dir.mkdir(parents=True, exist_ok=True)
out_file = out_dir / "readme-cover-openclaw-skills.png"
img.save(out_file)
print(out_file)
