from collections import defaultdict
from pathlib import Path

with open(Path(__file__).with_name("input")) as fp:
    inp = fp.read().strip()

lines = iter(inp.splitlines())

algo = [int(ch == "#") for ch in next(lines)]
next(lines)

pixels = defaultdict(lambda: i % 2)

for y, line in enumerate(lines):
    for x, ch in enumerate(line):
        pixels[x, y] = int(ch == "#")


def area(x, y):
    for ny in range(y - 1, y + 2):
        for nx in range(x - 1, x + 2):
            yield nx, ny


def mins(pixels):
    x = min(p[0] for p in pixels)
    y = min(p[1] for p in pixels)
    return x, y


def maxs(pixels):
    x = max(p[0] for p in pixels)
    y = max(p[1] for p in pixels)
    return x, y


def pprint(pixels):
    minx, miny = mins(pixels)
    maxx, maxy = maxs(pixels)
    for y in range(miny - 1, maxy + 2):
        for x in range(minx - 1, maxx + 2):
            print(".#"[pixels[x, y]], end="")
        print()
    print()


for i in range(2):
    new = pixels.copy()
    minx, miny = mins(pixels)
    maxx, maxy = maxs(pixels)
    # pprint(pixels)
    for y in range(miny - 1, maxy + 2):
        for x in range(minx - 1, maxx + 2):
            pixels[x, y]
    keys = list(pixels.keys())
    for pixel in keys:
        n = ""
        for pix in area(*pixel):
            n = f"{n}{pixels[pix]}"
        b = int(n, 2)
        ch = algo[b]
        new[pixel] = ch
    pixels = new

# pprint(pixels)

print(sum(pixels.values()))
