from collections import defaultdict
from pathlib import Path

with open(Path(__file__).with_name("test3")) as fp:
    inp = fp.read().strip()


cols = defaultdict(list)


def intersecting(ranges, nr):
    out = []
    for i, (r, on) in enumerate(ranges):
        if nr.stop <= r.start:
            continue
        if r.stop <= nr.start:
            continue
        out.append((i, (r, on)))
    return out


def contains(r1, r2):
    return r1.start <= r2.start and r1.stop >= r2.stop


def merge(ranges, nr, non):
    offset = 0
    intersects = intersecting(ranges, nr)
    if not intersects:
        ranges.append((nr, non))
        ranges.sort(key=lambda r: r[0].start)
        return
    added = False
    for i, (r, on) in intersects:
        if contains(nr, r):
            del ranges[i + offset]
            offset -= 1
        elif contains(r, nr):
            if on != non:
                before = range(r.start, nr.start), on
                after = range(nr.stop, r.stop), on
                ranges[i + offset : i + offset + 1] = [before, (nr, non), after]
            added = True
            break
        elif nr.stop > r.start:
            if non == on:
                new = range(nr.start, r.stop), on
                ranges[i + offset] = new
            else:
                replace = range(nr.stop, r.stop), on
                ranges[i + offset : i + offset + 1] = [(nr, non), replace]
            added = True
            break
        elif nr.start < r.stop:
            added = True
            if non == on:
                new = range(r.start, nr.stop), on
                ranges[i + offset] = new
            else:
                replace = range(r.start, nr.start), on
                ranges[i + offset : i + offset + 1] = [replace, (nr, non)]
                offset += 1
                if (r, on) != intersects[-1]:
                    print("WARN: BUTTHOLE")
        if not added:
            ranges.append((nr, non))
            ranges.sort(key=lambda r: r[0].start)


i = 0
for line in inp.splitlines():
    i += 1
    print(i)
    if i == 11:
        breakpoint()
    inst, args = line.split()
    on = inst == "on"
    args = tuple(
        range((s := [*map(int, arg[2:].split(".."))])[0], s[1] + 1)
        for arg in args.split(",")
    )
    xarg, yarg, zarg = args

    for x in xarg:
        for y in yarg:
            merge(cols[x, y], zarg, on)

ans = 0
print(len(cols))
i = 0
for col in cols.values():
    i += 1
    print(i)
    for r, on in col:
        if on:
            ans += len(r)

print(ans)
