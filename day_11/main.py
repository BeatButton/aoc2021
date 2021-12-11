from pathlib import Path

with open(Path(__file__).with_name("input")) as fp:
    inp = fp.read().strip()

es = [[int(c) for c in line] for line in inp.splitlines()]

h = len(es)
w = len(es[0])


def get_surrounding(ox, oy):
    for x in range(ox - 1, ox + 2):
        for y in range(oy - 1, oy + 2):
            if x >= 0 and y >= 0 and y < w and x < h and not (x == ox and y == oy):
                yield x, y


def flash(x, y):
    if (x, y) in flashed:
        return

    flashed.add((x, y))
    for x, y in get_surrounding(x, y):
        es[x][y] += 1
        if es[x][y] > 9:
            flash(x, y)


def step():
    for x, row in enumerate(es):
        for y, e in enumerate(row):
            row[y] += 1
            if row[y] > 9:
                flash(x, y)


flashed = set()

from itertools import count

for i in count(1):
    step()
    if len(flashed) == w * h:
        print(i)
        break
    for x, y in flashed:
        es[x][y] = 0
    flashed = set()
