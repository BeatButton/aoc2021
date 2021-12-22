from pathlib import Path

with open(Path(__file__).with_name("input")) as fp:
    inp = fp.read().strip()

ranges = []

minx = maxx = miny = maxy = minz = maxz = 0

for line in inp.splitlines():
    inst, args = line.split()
    on = inst == "on"
    args = tuple(
        range((s := [*map(int, arg[2:].split(".."))])[0], s[1] + 1)
        for arg in args.split(",")
    )
    xarg, yarg, zarg = args

    minx = min(minx, xarg.start)
    maxx = max(maxx, xarg.stop)
    miny = min(miny, yarg.start)
    maxy = max(maxy, yarg.stop)
    minz = min(minz, zarg.start)
    maxz = max(maxz, zarg.stop)

    ranges.append((args, on))

ans = 0
print(minx, maxx)
print(miny, maxy)
for x in range(minx, maxy):
    print(f"x = {x}")
    for y in range(miny, maxy):
        print(f"y = {y}")
        for z in range(minz, maxz):
            for (xr, yr, zr), on in ranges[::-1]:
                if x in xr and y in yr and z in zr:
                    ans += on
                    break

print(ans)
