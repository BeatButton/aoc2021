from pathlib import Path
from itertools import cycle

with open(Path(__file__).with_name("input")) as fp:
    inp = fp.read().strip()

lines = iter(inp.splitlines())
p1 = int(next(lines)[-1])
s1 = 0
p2 = int(next(lines)[-1])
s2 = 0
die = cycle(range(1, 101))

c = 0
while True:
    for _ in range(3):
        p1 += next(die)
        c += 1
    p1 = (p1 - 1) % 10 + 1
    s1 += p1

    if s1 >= 1000:
        break

    for _ in range(3):
        p2 += next(die)
        c += 1
    p2 = (p2 - 1) % 10 + 1
    s2 += p2

    if s2 >= 1000:
        break
    print(s1)
    print(s2)

print(min(s1, s2) * c)
