class Grid(list):
    def __init__(self, factory=int):
        self.factory = factory

    def _validate(self, index):
        if isinstance(index, int):
            diff = index - len(self) + 1
            if diff > 0:
                self.extend([self.factory() for _ in range(diff)])

    def __getitem__(self, index):
        self._validate(index)
        return super().__getitem__(index)

    def __setitem__(self, index, value):
        self._validate(index)
        return super().__setitem__(index, value)


class Grid2D(Grid):
    def __init__(self, factory=int):
        self.factory = lambda: Grid(factory)
