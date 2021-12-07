from pathlib import Path

with open(Path(__file__).with_name("input")) as fp:
    inp = fp.read().strip()

crabs = eval(f"[{inp}]")
crabs.sort()

L = len(crabs)
half = L // 2 - 1

if L % 2 == 0:
    med = (crabs[half] + crabs[half + 1]) // 2
else:
    med = crabs[half]

print(med)
ans = sum(abs(crab - med) for crab in crabs)

print(ans)
