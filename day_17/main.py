from pathlib import Path
from itertools import count

with open(Path(__file__).with_name("input")) as fp:
    inp = fp.read().strip()

xi, yi = inp.split()[2:]
xr = range(*map(int, xi[2:-1].split("..")))
yr = range(*map(int, yi[2:].split("..")))

mmy = 0
for odx in count():
    for dy in range(-100, 100):
        dx = odx
        x = y = my = 0
        while True:
            x += dx
            y += dy
            dy -= 1
            if dx > 0:
                dx -= 1
            elif dx < 0:
                dx += 1
            my = max(y, my)
            if x in xr and y in yr:
                if my > mmy:
                    mmy = my
                    print(mmy)
                break
            elif y < yr.start:
                break
