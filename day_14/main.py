from collections import Counter, defaultdict
from pathlib import Path

with open(Path(__file__).with_name("test")) as fp:
    inp = fp.read().strip()

lines = iter(inp.splitlines())
init = next(lines)

state = defaultdict(int)

start = init[:2]
end = init[-2:]
for a, b in zip(init, init[1:]):
    state[a + b] += 1

next(lines)
rules = {}
for line in lines:
    pair, insert = line.split(" -> ")
    rules[pair] = (pair[0] + insert, insert + pair[1])


for i in range(40):
    new = state.copy()
    start = rules[start][0]
    end = rules[end][1]
    for pair, amt in state.items():
        for add in rules[pair]:
            new[add] += amt
        new[pair] -= amt
    state = new

c = Counter()

m = len(state)
for i, (pair, amt) in enumerate(state.items()):
    c[pair[0]] += amt
    c[pair[1]] += amt

c[start[0]] += 1
c[end[1]] += 1
com = c.most_common()
ans = com[0][1] // 2 - com[-1][1] // 2

print(ans)
