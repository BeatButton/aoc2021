from pathlib import Path

with open(Path(__file__).with_name("input")) as fp:
    inp = fp.read().strip()

lines = iter(inp.splitlines())
state = list(next(lines))
next(lines)
rules = {}
for line in lines:
    pair, insert = line.split(" -> ")
    rules[pair] = insert


for i in range(10):
    inserts = [""] * (len(state) - 1)
    for j, (a, b) in enumerate(zip(state, state[1:])):
        if r := rules.get(a + b):
            inserts[j] = r
    new_state = []
    for a, b in zip(state, inserts):
        new_state.append(a)
        if b:
            new_state.append(b)
    state = new_state + [state[-1]]

from collections import Counter

c = Counter(state)
com = c.most_common()
ans = com[0][1] - com[-1][1]
print(ans)
