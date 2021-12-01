from pathlib import Path

with open(Path(__file__).with_name("input")) as fp:
    inp = fp.read().strip()


inp = [int(l) for l in inp.split()]

count = -1
last = 0
for a, b, c in zip(inp, inp[1:], inp[2:]):
    s = a + b + c
    if s > last:
        count += 1
    last = s


print(count)
