from pathlib import Path

with open(Path(__file__).with_name("input")) as fp:
    inp = fp.read().strip()


pts = {")": 3, "]": 57, "}": 1197, ">": 25137}


m = dict(zip("([{<", ")]}>"))
opens = list(m)

lines = inp.splitlines()
rest = []
for line in lines:
    stack = []
    for c in line:
        if c in m:
            stack.append(c)
        elif c != m[stack.pop()]:
            break
    else:
        rest.append(stack)

scores = []
for stack in rest:
    score = 0
    for c in stack[::-1]:
        score *= 5
        score += opens.index(c) + 1
    scores.append(score)

scores.sort()
print(scores[len(scores) // 2])
