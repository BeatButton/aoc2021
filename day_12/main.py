from pathlib import Path

with open(Path(__file__).with_name("input")) as fp:
    inp = fp.read().strip()


from collections import defaultdict

m = defaultdict(list)

from string import ascii_lowercase

small = set(ascii_lowercase)

for line in inp.splitlines():
    f, t = line.split("-")
    if t != "start":
        m[f].append(t)
    if f != "start":
        m[t].append(f)


def visit(now, orig_seen, path):
    nexts = m[now]
    for n in filter(lambda n: not n in orig_seen, nexts):
        seen = orig_seen.copy()
        if n == "end":
            yield path + [n]
            continue
        if set(n) < small:
            seen |= {n}
        yield from visit(n, seen, path + [n])


paths = list(visit("start", set(), ["start"]))


print(len(paths))
