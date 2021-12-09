from pathlib import Path


with open(Path(__file__).with_name("input")) as fp:
    inp = fp.read().strip()


data = [[int(ch) for ch in line] for line in inp.splitlines()]

w = len(data[0])
h = len(data)


def get_surrounding(x, y):
    return filter(
        (lambda p: p[0] >= 0 and p[1] >= 0 and p[1] < w and p[0] < h),
        [[x + 1, y], [x - 1, y], [x, y - 1], [x, y + 1]],
    )


def is_risk(x, y):
    return all(data[nx][ny] > data[x][y] for nx, ny in get_surrounding(x, y))


ans = 0
for x, row in enumerate(data):
    for y, val in enumerate(row):
        if is_risk(x, y):
            ans += val + 1


print(ans)
