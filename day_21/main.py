from pathlib import Path
from functools import lru_cache


def start(p1, p2):
    return (
        roll11(p1, 0, p2, 0, r=1)
        + roll11(p1, 0, p2, 0, r=2)
        + roll11(p1, 0, p2, 0, r=3)
    )


@lru_cache(maxsize=None)
def roll11(p1, s1, p2, s2, r):
    return (
        roll12(p1, s1, p2, s2, r=r + 1)
        + roll12(p1, s1, p2, s2, r=r + 2)
        + roll12(p1, s1, p2, s2, r=r + 3)
    )


@lru_cache(maxsize=None)
def roll12(p1, s1, p2, s2, r):
    return (
        roll13(p1, s1, p2, s2, r=r + 1)
        + roll13(p1, s1, p2, s2, r=r + 2)
        + roll13(p1, s1, p2, s2, r=r + 3)
    )


@lru_cache(maxsize=None)
def roll13(p1, s1, p2, s2, r):
    p1 += r
    p1 = (p1 - 1) % 10 + 1
    s1 += p1
    if s1 >= 21:
        return 1
    return (
        roll21(p1, s1, p2, s2, r=1)
        + roll21(p1, s1, p2, s2, r=2)
        + roll21(p1, s1, p2, s2, r=3)
    )


@lru_cache(maxsize=None)
def roll21(p1, s1, p2, s2, r):
    return (
        roll22(p1, s1, p2, s2, r=r + 1)
        + roll22(p1, s1, p2, s2, r=r + 2)
        + roll22(p1, s1, p2, s2, r=r + 3)
    )


@lru_cache(maxsize=None)
def roll22(p1, s1, p2, s2, r):
    return (
        roll23(p1, s1, p2, s2, r=r + 1)
        + roll23(p1, s1, p2, s2, r=r + 2)
        + roll23(p1, s1, p2, s2, r=r + 3)
    )


@lru_cache(maxsize=None)
def roll23(p1, s1, p2, s2, r):
    p2 += r
    p2 = (p2 - 1) % 10 + 1
    s2 += p2
    if s2 >= 21:
        return 1j
    return (
        roll11(p1, s1, p2, s2, r=1)
        + roll11(p1, s1, p2, s2, r=2)
        + roll11(p1, s1, p2, s2, r=3)
    )


with open(Path(__file__).with_name("input")) as fp:
    inp = fp.read().strip()

lines = iter(inp.splitlines())
a = int(next(lines)[-1])
b = int(next(lines)[-1])

ans = start(a, b)
print(max(ans.imag, ans.real))
