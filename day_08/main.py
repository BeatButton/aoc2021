from pathlib import Path
from itertools import permutations

with open(Path(__file__).with_name("input")) as fp:
    inp = fp.read().strip()

canonical_digits = [
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg",
]

ans = 0
for line in inp.splitlines():
    left, right = map(str.split, line.split("|"))
    for guess in permutations("abcdefg"):
        trans = str.maketrans("".join(guess), "abcdefg")
        for digit in left:
            t_digit = "".join(sorted(digit.translate(trans)))
            if t_digit not in canonical_digits:
                break
        else:
            for idx, digit in enumerate(right[::-1]):
                t_digit = "".join(sorted(digit.translate(trans)))
                ans += canonical_digits.index(t_digit) * 10 ** idx
            break


print(ans)
