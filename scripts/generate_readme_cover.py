from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

W, H = 1600, 560
img = Image.new("RGB", (W, H), "#0b0c10")
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import random

W, H = 1366, 402
img = Image.new("RGB", (W, H), "#07090f")
d = ImageDraw.Draw(img)

# 背景渐变（左偏紫红 -> 右偏深蓝）
for x in range(W):
    t = x / (W - 1)
    r = int(22 * (1 - t) + 0 * t)
    g = int(8 * (1 - t) + 25 * t)
    b = int(28 * (1 - t) + 35 * t)
    d.line((x, 0, x, H), fill=(r, g, b))

# 大范围柔光
overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
od = ImageDraw.Draw(overlay)
for cx, cy, rad, color in [
    (110, 220, 290, (255, 65, 85, 70)),
    (1240, 260, 320, (0, 220, 210, 60)),
    (680, 90, 210, (120, 0, 255, 35)),
]:
    for i in range(rad, 0, -6):
        a = int(color[3] * (i / rad) ** 2)
        od.ellipse((cx - i, cy - i, cx + i, cy + i), fill=(color[0], color[1], color[2], a))
img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
d = ImageDraw.Draw(img)

# 星点
random.seed(42)
for _ in range(22):
    x = random.randint(20, W - 20)
    y = random.randint(16, H - 24)
    r = random.choice([1, 1, 2])
    col = random.choice([(255, 255, 255), (110, 250, 255), (255, 120, 140)])
    d.ellipse((x - r, y - r, x + r, y + r), fill=col)

# 吉祥物外发光
overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
od = ImageDraw.Draw(overlay)
cx, cy = 680, 95
for i in range(145, 0, -4):
    a = int(80 * (i / 145) ** 2)
    od.ellipse((cx - i, cy - i, cx + i, cy + i), fill=(255, 40, 70, a))
img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
d = ImageDraw.Draw(img)

# 吉祥物（简化龙虾风）
d.ellipse((cx - 88, cy - 78, cx + 88, cy + 92), fill="#ff4f57")
d.ellipse((cx - 58, cy - 126, cx + 58, cy - 30), fill="#ff5d64")
d.ellipse((cx - 36, cy - 68, cx - 14, cy - 46), fill="#121826")
d.ellipse((cx + 14, cy - 68, cx + 36, cy - 46), fill="#121826")
d.ellipse((cx - 31, cy - 63, cx - 24, cy - 56), fill="#4affdf")
d.ellipse((cx + 20, cy - 63, cx + 27, cy - 56), fill="#4affdf")
d.line((cx - 18, cy - 122, cx - 44, cy - 145), fill="#ff8087", width=5)
d.line((cx + 18, cy - 122, cx + 44, cy - 145), fill="#ff8087", width=5)
d.ellipse((cx - 97, cy - 36, cx - 54, cy + 8), fill="#ef4651")
d.ellipse((cx + 54, cy - 36, cx + 97, cy + 8), fill="#ef4651")
d.rectangle((cx - 20, cy + 72, cx - 2, cy + 96), fill="#e2424b")
d.rectangle((cx + 2, cy + 72, cx + 20, cy + 96), fill="#e2424b")

# 字体
font_candidates = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
]


def pick_font(size: int):
    for p in font_candidates:
        if Path(p).exists():
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()


# OpenClaw 渐变字
text = "OpenClaw"
font = pick_font(108)
mask = Image.new("L", (W, H), 0)
md = ImageDraw.Draw(mask)
text_w = int(md.textlength(text, font=font))
text_x = (W - text_w) // 2
text_y = 255
md.text((text_x, text_y), text, font=font, fill=255)

grad = Image.new("RGB", (W, H), 0)
gd = ImageDraw.Draw(grad)
for x in range(W):
    t = (x - text_x) / max(1, text_w)
    t = max(0.0, min(1.0, t))
    r = int(233 + (255 - 233) * t)
    g = int(171 + (74 - 171) * t)
    b = int(190 + (87 - 190) * t)
    gd.line((x, 0, x, H), fill=(r, g, b))
img.paste(grad, mask=mask)

# 细边框
d = ImageDraw.Draw(img)
d.rectangle((0, 0, W - 1, H - 1), outline="#1b2330", width=2)

out_dir = Path("/Users/wudengyao/openclaw-setup-playbook-zh/assets")
out_dir.mkdir(parents=True, exist_ok=True)
out_file = out_dir / "readme-cover-openclaw-skills.png"
img.save(out_file)
print(out_file)
