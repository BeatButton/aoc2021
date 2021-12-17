from pathlib import Path
from itertools import count

with open(Path(__file__).with_name("input")) as fp:
    inp = fp.read().strip()

xi, yi = inp.split()[2:]
xf, xt = map(int, xi[2:-1].split(".."))
xr = range(xf, xt + 1)
yf, yt = map(int, yi[2:].split(".."))
yr = range(yf, yt + 1)

tot = 0
for odx in count():
    for dy in range(-100, 100):
        dx = odx
        x = y = 0
        while True:
            x += dx
            y += dy
            dy -= 1
            if dx > 0:
                dx -= 1
            elif dx < 0:
                dx += 1
            if x in xr and y in yr:
                tot += 1
                print(tot)
                break
            elif y < yr.start:
                break
