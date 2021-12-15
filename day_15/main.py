from dataclasses import dataclass
from pathlib import Path

with open(Path(__file__).with_name("test")) as fp:
    inp = fp.read().strip()

INF = float("inf")


def adj(xy):
    x, y = xy
    return [(x + 1, y), (x, y + 1)]


grid = {}
dist = {}
for y, line in enumerate(inp.splitlines()):
    for x, cost in enumerate(map(int, line)):
        grid[x, y] = cost
        dist[x, y] = INF

curr = 0, 0
dist[curr] = grid[curr]
unvisited = [(nx, ny) for nx in range(x) for ny in range(y)]

while unvisited:
    curr = unvisited.pop()
    for nxt in adj(curr):
        try:
            cost = grid[nxt]
        except KeyError:
            continue
        dist[nxt] = dist[curr] + cost
    unvisited.sort(key=lambda p: dist[p], reverse=True)

print(dist[x - 1, y - 1])
