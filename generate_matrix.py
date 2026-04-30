import random
import math

WIDTH = 800
HEIGHT = 200
COLS = 40
FONT_SIZE = 14
COL_WIDTH = WIDTH / COLS
CHARS = "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン0123456789ABCDEF"

random.seed(42)

drops = []
for i in range(COLS):
    drops.append({
        "x": i * COL_WIDTH + COL_WIDTH / 2,
        "delay": random.uniform(0, 3),
        "speed": random.uniform(1.5, 3.5),
        "length": random.randint(5, 15),
        "chars": [random.choice(CHARS) for _ in range(20)]
    })

svg_parts = []
svg_parts.append(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');
    </style>
    <clipPath id="clip">
      <rect width="{WIDTH}" height="{HEIGHT}"/>
    </clipPath>
    <filter id="glow">
      <feGaussianBlur stdDeviation="2" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="{WIDTH}" height="{HEIGHT}" fill="#0D1117"/>
  <g clip-path="url(#clip)">''')

for drop in drops:
    x = drop["x"]
    delay = drop["delay"]
    speed = drop["speed"]
    length = drop["length"]
    chars = drop["chars"]
    duration = speed
    total_distance = HEIGHT + length * FONT_SIZE

    for j in range(length):
        char = chars[j % len(chars)]
        opacity_factor = (length - j) / length
        if j == 0:
            color = "#FFFFFF"
            opacity = 1.0
            blur = "filter=\"url(#glow)\""
        elif j < 3:
            color = "#00FF41"
            opacity = round(0.9 - j * 0.1, 2)
            blur = "filter=\"url(#glow)\""
        else:
            color = "#00AA2A"
            opacity = round(opacity_factor * 0.7, 2)
            blur = ""

        char_delay = delay
        char_duration = duration + speed * 2

        svg_parts.append(f'''
    <text
      x="{x}"
      y="0"
      font-family="'Share Tech Mono', monospace"
      font-size="{FONT_SIZE}"
      fill="{color}"
      opacity="{opacity}"
      text-anchor="middle"
      {blur}
    >
      {char}
      <animateTransform
        attributeName="transform"
        type="translate"
        from="0 {-(j * FONT_SIZE)}"
        to="0 {total_distance - (j * FONT_SIZE)}"
        dur="{char_duration:.1f}s"
        begin="{char_delay:.2f}s"
        repeatCount="indefinite"
      />
      <animate
        attributeName="opacity"
        values="{opacity};{opacity};0"
        keyTimes="0;0.85;1"
        dur="{char_duration:.1f}s"
        begin="{char_delay:.2f}s"
        repeatCount="indefinite"
      />
    </text>''')

# Overlay gradient for text readability
svg_parts.append(f'''
  </g>
  <defs>
    <linearGradient id="textBg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0D1117" stop-opacity="0"/>
      <stop offset="40%" stop-color="#0D1117" stop-opacity="0.3"/>
      <stop offset="60%" stop-color="#0D1117" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#0D1117" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#textBg)"/>''')

# Main name text - SAMET ARI
svg_parts.append(f'''
  <text
    x="{WIDTH/2}"
    y="{HEIGHT/2 - 10}"
    font-family="'Share Tech Mono', monospace"
    font-size="42"
    font-weight="bold"
    fill="#7C3AED"
    text-anchor="middle"
    dominant-baseline="middle"
    filter="url(#glow)"
    letter-spacing="8"
  >
    SAMET ARI
    <animate
      attributeName="opacity"
      values="0.8;1;0.8"
      dur="3s"
      repeatCount="indefinite"
    />
  </text>''')

# Subtitle
svg_parts.append(f'''
  <text
    x="{WIDTH/2}"
    y="{HEIGHT/2 + 35}"
    font-family="'Share Tech Mono', monospace"
    font-size="13"
    fill="#00FF41"
    text-anchor="middle"
    dominant-baseline="middle"
    letter-spacing="3"
    opacity="0.85"
  >
    SYSTEM &amp; NETWORK ADMINISTRATOR | CYBERSECURITY
    <animate
      attributeName="opacity"
      values="0.6;0.9;0.6"
      dur="2.5s"
      begin="0.5s"
      repeatCount="indefinite"
    />
  </text>
</svg>''')

svg_content = "\n".join(svg_parts)

with open("dist/matrix-header.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

print("matrix-header.svg generated successfully!")
