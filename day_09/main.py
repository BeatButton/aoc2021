from pathlib import Path

from functools import reduce
from operator import mul

with open(Path(__file__).with_name("input")) as fp:
    inp = fp.read().strip()


data = [[int(ch) for ch in line] for line in inp.splitlines()]

w = len(data[0])
h = len(data)


def get_surrounding(x, y):
    return filter(
        (lambda p: p[0] >= 0 and p[1] >= 0 and p[1] < w and p[0] < h),
        [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)],
    )


def is_low(x, y):
    return all(data[nx][ny] > data[x][y] for nx, ny in get_surrounding(x, y))


basins = []
for x, row in enumerate(data):
    for y, val in enumerate(row):
        if is_low(x, y):
            if any((x, y) in basin for basin in basins):
                print("odd!")
                continue
            basin = set()
            check = [(x, y)]
            while check:
                cx, cy = check.pop()
                basin.add((cx, cy))
                for nx, ny in get_surrounding(cx, cy):
                    if (nx, ny) not in basin and data[nx][ny] != 9:
                        check.append((nx, ny))
            basins.append(basin)


ans = reduce(mul, map(len, sorted(basins, key=len)[-3:]))
print(ans)
