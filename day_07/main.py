from pathlib import Path

with open(Path(__file__).with_name("input")) as fp:
    inp = fp.read().strip()

crabs = eval(f"[{inp}]")
crabs.sort()

min_ans = 99 ** 99
for avg in range(0, crabs[-1]):
    ans = 0

    for crab in crabs:
        if crab == avg:
            continue
        elif crab < avg:
            delta = 1
        else:
            delta = -1
        step = 1
        while crab != avg:
            crab += delta
            ans += step
            step += 1
    if ans < min_ans:
        min_ans = ans
    print(f"{avg}: {min_ans}")
