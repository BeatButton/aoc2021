from __future__ import annotations
from os import popen

from pathlib import Path
from dataclasses import dataclass
from itertools import permutations

with open(Path(__file__).with_name("input")) as fp:
    inp = fp.read().strip()


@dataclass
class Point:
    __slots__ = ("x", "y", "z")
    x: int
    y: int
    z: int

    def __add__(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Point) -> Point:
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def rotate_x(self, times) -> Point:
        p = Point(self.x, self.y, self.z)
        for _ in range(times):
            p.y, p.z = -p.z, p.y
        return p

    def rotate_y(self, times) -> Point:
        p = Point(self.x, self.y, self.z)
        for _ in range(times):
            p.x, p.z = -p.z, p.x
        return p

    def rotate_z(self, times) -> Point:
        p = Point(self.x, self.y, self.z)
        for _ in range(times):
            p.x, p.y = -p.y, p.x
        return p

    def flip_z(self) -> Point:
        return Point(self.y, self.x, -self.z)


scanners: list[set[Point]] = []
reality: set[Point] = set()
scanners_ind: list[tuple[Point, set[Point]]] = []
for segment in inp.split("\n\n"):
    scanner: set[Point] = set()
    for line in segment.splitlines()[1:]:
        scanner.add(Point(*map(int, line.split(","))))
    if not reality:
        reality = scanner
        scanners_ind.append((Point(0, 0, 0), scanner))
    else:
        scanners.append(scanner)


while scanners:
    print(f"{len(scanners)} scanners left...")
    for i, o_scanner in enumerate(scanners):
        for x_rot, y_rot in [(0, 1), (1, 0), (0, 0)]:
            if x_rot:
                r_scanner = set(p.rotate_x(1) for p in o_scanner)
            elif y_rot:
                r_scanner = set(p.rotate_y(1) for p in o_scanner)
            else:
                r_scanner = o_scanner
            for flip in [False, True]:
                if flip:
                    f_scanner = set(p.flip_z() for p in r_scanner)
                else:
                    f_scanner = r_scanner
                for z_rot in range(4):
                    z_scanner = set(p.rotate_z(z_rot) for p in f_scanner)
                    for reality_reference in reality:
                        for point in z_scanner:
                            trans = reality_reference - point
                            t_scanner = set(point + trans for point in z_scanner)
                            if len(t_scanner & reality) >= 12:
                                scanners_ind.append((trans, t_scanner))
                                reality |= t_scanner
                                break
                        else:
                            continue
                        break
                    else:
                        continue
                    break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        break
    else:
        print(f"could not find a match with {len(scanners)} scanners left")
        break
    del scanners[i]

print(len(reality))
