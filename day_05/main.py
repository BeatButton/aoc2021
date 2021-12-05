from collections import defaultdict
from pathlib import Path

import operator

with open(Path(__file__).with_name("input")) as fp:
    inp = fp.read().strip()

points = defaultdict(int)

for line in inp.splitlines():

    p1, p2 = line.split(" -> ")
    x1, y1 = map(int, p1.split(","))
    x2, y2 = map(int, p2.split(","))
    if x1 == x2:
        if y2 < y1:
            y1, y2 = y2, y1
        for y in range(y1, y2 + 1):
            points[(x1, y)] += 1
    elif y1 == y2:
        if x2 < x1:
            x1, x2 = x2, x1
        for x in range(x1, x2 + 1):
            points[(x, y1)] += 1
    else:
        x = x1
        y = y1
        Δx = 1 if x1 < x2 else -1
        Δy = 1 if y1 < y2 else -1
        cond = operator.le if Δx == 1 else operator.ge
        while cond(x, x2):
            points[(x, y)] += 1
            x += Δx
            y += Δy


print(sum(n >= 2 for n in points.values()))
