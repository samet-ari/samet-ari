import random

WIDTH = 800
HEIGHT = 200
COLS = 55
FONT_SIZE = 13
COL_WIDTH = WIDTH / COLS
CHARS = "アイウエオカキクケコサシスセソタチツテトナニヌネノ0123456789ABCDEF"

random.seed(99)

lines = []
lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">')
lines.append(f'  <rect width="{WIDTH}" height="{HEIGHT}" fill="#0D1117"/>')

# Generate matrix rain columns using CSS animations only
lines.append('  <style>')
lines.append('    .col { font-family: monospace; font-size: 13px; }')

# Generate keyframes for each column
for i in range(COLS):
    delay = random.uniform(0, 4)
    duration = random.uniform(2, 5)
    lines.append(f'    @keyframes fall{i} {{ 0% {{ transform: translateY(-150px); opacity: 1; }} 100% {{ transform: translateY({HEIGHT + 50}px); opacity: 0; }} }}')

lines.append('    .name-text { animation: pulse 2s ease-in-out infinite; }')
lines.append('    @keyframes pulse { 0%,100% { opacity: 0.85; } 50% { opacity: 1; } }')
lines.append('    .sub-text { animation: pulse2 2.5s ease-in-out infinite; }')
lines.append('    @keyframes pulse2 { 0%,100% { opacity: 0.6; } 50% { opacity: 0.9; } }')
lines.append('  </style>')

lines.append('  <clipPath id="clip"><rect width="{}" height="{}"/></clipPath>'.format(WIDTH, HEIGHT))
lines.append('  <g clip-path="url(#clip)">')

# Draw matrix columns
for i in range(COLS):
    x = i * COL_WIDTH + COL_WIDTH / 2
    delay = round(random.uniform(0, 4), 2)
    duration = round(random.uniform(2, 5), 2)
    length = random.randint(4, 10)

    for j in range(length):
        char = random.choice(CHARS)
        if j == 0:
            color = "#FFFFFF"
            opacity = 1.0
        elif j < 3:
            color = "#00FF41"
            opacity = round(0.85 - j * 0.1, 2)
        else:
            color = "#00AA2A"
            opacity = round(0.5 - (j * 0.03), 2)
            opacity = max(opacity, 0.1)

        y_offset = j * FONT_SIZE
        lines.append(f'    <text x="{x:.1f}" y="{y_offset}" text-anchor="middle" fill="{color}" opacity="{opacity}" style="font-family:monospace;font-size:{FONT_SIZE}px;animation:fall{i} {duration}s {delay}s linear infinite;">{char}</text>')

lines.append('  </g>')

# Dark overlay for readability
lines.append(f'  <rect width="{WIDTH}" height="{HEIGHT}" fill="#0D1117" opacity="0.45"/>')

# Centered name
lines.append(f'  <text x="{WIDTH//2}" y="{HEIGHT//2 - 8}" text-anchor="middle" dominant-baseline="middle" fill="#A78BFA" font-family="monospace" font-size="44" font-weight="bold" letter-spacing="10" class="name-text">SAMET ARI</text>')

# Subtitle
lines.append(f'  <text x="{WIDTH//2}" y="{HEIGHT//2 + 32}" text-anchor="middle" dominant-baseline="middle" fill="#00FF41" font-family="monospace" font-size="12" letter-spacing="3" class="sub-text">SYSTEM &amp; NETWORK ADMINISTRATOR | CYBERSECURITY</text>')

lines.append('</svg>')

svg = "\n".join(lines)

import os
os.makedirs("dist", exist_ok=True)
with open("dist/matrix-header.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("Done! matrix-header.svg generated.")
