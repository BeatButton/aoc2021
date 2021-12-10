from pathlib import Path

with open(Path(__file__).with_name("input")) as fp:
    inp = fp.read().strip()


stack = []

pts = {")": 3, "]": 57, "}": 1197, ">": 25137}

m = dict(zip("([{<", ")]}>"))

ans = 0
for line in inp:
    for c in line.strip():
        if c in m:
            stack.append(c)
        elif c != m[stack.pop()]:
            ans += pts[c]
            break

print(ans)
