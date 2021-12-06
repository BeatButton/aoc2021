from pathlib import Path

with open(Path(__file__).with_name("input")) as fp:
    inp = fp.read().strip()


timers = [0] * 9

for n in map(int, inp.split(",")):
    timers[n] += 1


def tick():
    new = timers[0]
    for i, j in zip(range(8), range(1, 9)):
        timers[i] = timers[j]
    timers[8] = new
    timers[6] += new


for i in range(256):
    tick()

print(sum(timers))
