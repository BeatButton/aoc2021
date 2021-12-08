from pathlib import Path
from itertools import permutations

with open(Path(__file__).with_name("input")) as fp:
    inp = fp.read().strip()

# fmt: off
_canonical_digits = [
    [0, 1, 2, 4, 5, 6],    # 0
    [2, 5],                # 1
    [0, 2, 3, 4, 6],       # 2
    [0, 2, 3, 5, 6],       # 3
    [1, 2, 3, 5],          # 4
    [0, 1, 3, 5, 6],       # 5
    [0, 1, 3, 4, 5, 6],    # 6
    [0, 2, 5],             # 7
    [0, 1, 2, 3, 4, 5, 6], # 8
    [0, 1, 2, 3, 5, 6],    # 9
]
# fmt: on
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
    left, right = map(str.strip, line.split("|"))
    for guess in permutations("abcdefg"):
        trans = str.maketrans("".join(guess), "abcdefg")
        for i, digit in enumerate(left.split()):
            t_digit = "".join(sorted(digit.translate(trans)))
            if t_digit not in canonical_digits:
                break

        else:
            this_line = 0
            for idx, digit in enumerate(right.split()[::-1]):
                t_digit = "".join(sorted(digit.translate(trans)))
                this_line += canonical_digits.index(t_digit) * 10 ** idx

            ans += this_line


print(ans)
