from pathlib import Path

with open(Path(__file__).with_name("input")) as fp:
    inp = fp.read().strip()


class Fish:
    def __init__(self, timer=8):
        self.timer = timer

    def __repr__(self):
        return str(self.timer)


fish = []

for n in map(int, inp.split(",")):
    fish.append(Fish(n))


def tick():
    new = 0
    for f in fish:
        if f.timer == 0:
            f.timer = 6
            new += 1
        else:
            f.timer -= 1
    fish.extend(Fish() for _ in range(new))


for i in range(80):
    print(i)
    tick()

print(len(fish))
