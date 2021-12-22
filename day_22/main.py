from pathlib import Path
from collections import defaultdict

with open(Path(__file__).with_name("input")) as fp:
    inp = fp.read().strip()

cube = defaultdict(int)

for line in inp.splitlines():
    inst, args = line.split()
    on = inst == "on"
    args = tuple(
        range((s := [*map(int, arg[2:].split(".."))])[0], s[1] + 1)
        for arg in args.split(",")
    )
    xarg, yarg, zarg = args
    if any(arg.start < -50 or arg.start > 50 for arg in args):
        continue
    for x in xarg:
        for y in yarg:
            for z in zarg:
                cube[x, y, z] = on

print(sum(cube.values()))
