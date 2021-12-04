from pathlib import Path


class Space:
    def __init__(self, val, down, over):
        self.val = val
        self.down = down
        self.over = over
        self.hit = False

    def __repr__(self):
        out = str(self.val)
        if self.hit:
            out = f"*{out}"
        return out


class Board:
    row_map: dict[int, Space]
    spaces: list[list[Space]]

    def __init__(self, board: list[str]):
        row_map = {}
        spaces: list[list[Space]] = []
        for over, row in enumerate(board):
            spacerow: list[Space] = []
            for down, val in enumerate(map(int, row.split())):
                s = Space(val, down, over)
                row_map[val] = s
                spacerow.append(s)
            spaces.append(spacerow)
        self.row_map = row_map
        self.spaces = spaces

    @property
    def winning(self):
        for row in self.spaces:
            if all(s.hit for s in row):
                return True

        for col in zip(*self.spaces):
            if all(s.hit for s in col):
                return True

    @property
    def score(self):
        return sum(space.val for space in self.row_map.values() if not space.hit)

    def __repr__(self):
        return repr(self.spaces)


with open(Path(__file__).with_name("input")) as fp:
    inp = fp.read().strip()

lines = inp.splitlines()

calls = eval(f"[{lines[0]}]")

i = 2
boards: list[Board] = []
while i < len(lines):
    boards.append(Board(lines[i : i + 5]))
    i += 6

loser = None
for i in range(len(calls)):
    call = calls[i]
    print(call)
    for board in boards:
        if space := board.row_map.get(call):
            space.hit = True
    loser = None
    for board in boards:
        if not board.winning:
            if loser is None:
                loser = board
            else:
                break
    else:
        break

assert loser is not None

while True:
    i += 1
    call = calls[i]
    print(call)
    if space := loser.row_map.get(call):
        space.hit = True
    if loser.winning:
        break

print(loser.score * call)
