from pathlib import Path

with open(Path(__file__).with_name("input")) as fp:
    inp = fp.read().strip()


lines = inp.splitlines()
LEN = len(lines[0])
counts = [0] * LEN

for line in lines:
    for i, ch in enumerate(line):
        counts[i] += 1 if ch == "1" else -1

gamma = int("".join("1" if v > 0 else "0" for v in counts), 2)
epsilon = int("".join("1" if v < 0 else "0" for v in counts), 2)


os = lines[:]
for i in range(LEN):
    v = 0
    for o in os:
        v += 1 if o[i] == "1" else -1
    ch = "1" if v >= 0 else "0"
    os = [o for o in os if o[i] == ch]
    if len(os) == 1:
        break

o = os[0]
print(f"o = {o}")

cs = lines[:]
for i in range(LEN):
    v = 0
    for c in cs:
        v += 1 if c[i] == "1" else -1
    ch = "0" if v >= 0 else "1"
    cs = [c for c in cs if c[i] == ch]
    if len(cs) == 1:
        break

c = cs[0]
print(f"c = {c}")

print(int(o, 2) * int(c, 2))
