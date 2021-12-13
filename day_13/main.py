from collections import defaultdict
from pathlib import Path

with open(Path(__file__).with_name("input")) as fp:
    inp = fp.read().strip()


grid = defaultdict(lambda: defaultdict(int))

it = iter(inp.splitlines())
num = 0
w = 0
h = 0
for line in it:
    if not line:
        break
    x, y = map(int, line.split(","))
    grid[y][x] = 1
    w = max(w, x)
    h = max(h, y)
    num += 1

h += 1
w += 1
folds = list(it)


for fold in folds:
    direction, value = fold.split(" ")[2].split("=")
    value = int(value)
    if direction == "y":
        for y in range(value):
            for x in range(w):
                grid[y][x] += grid[2 * value - y][x]
        h //= 2
    elif direction == "x":
        for y in range(h):
            for x in range(value):
                grid[y][x] += grid[y][2 * value - x]
        w //= 2
    else:
        print("you fucking idiot")


for y in range(h):
    for x in range(w):
        if grid[y][x]:
            print("#", end="")
        else:
            print(".", end="")
            pass
    print()
