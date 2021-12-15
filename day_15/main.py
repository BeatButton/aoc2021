from pathlib import Path
import heapq

with open(Path(__file__).with_name("input")) as fp:
    inp = fp.read().strip()

INF = float("inf")


def adj(xy):
    x, y = xy
    return [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]


grid = {}
dist = {}
unvisited = []
for y, line in enumerate(inp.splitlines()):
    for x, cost in enumerate(map(int, line)):
        grid[x, y] = cost
        dist[x, y] = INF
        unvisited.append((x, y))

dist[0, 0] = 0
unvisited[:] = unvisited[1:] + [(0, 0)]  # lol

while unvisited:
    curr = unvisited.pop()
    for nxt in adj(curr):
        try:
            cost = grid[nxt]
        except KeyError:
            continue
        dist[nxt] = min(dist[nxt], dist[curr] + cost)
    unvisited.sort(key=lambda p: dist[p], reverse=True)


print(dist[max(grid)])
