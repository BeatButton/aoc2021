from pathlib import Path

with open(Path(__file__).with_name("input")) as fp:
    inp = fp.read().strip()


x = 0
y = 0
aim = 0
for line in inp.split("\n"):
    c, v = line.split()
    v = int(v)
    match c:
        case "forward":
            x += v
            y += v * aim
        case "backward":
            x -= v
            y -= v * aim
        case "up":
            aim -= v
        case "down":
            aim += v
        case other:
            print(f"fuck!!! {other}")
            raise Exception

print(x * y)
