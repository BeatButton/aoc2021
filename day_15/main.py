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
for y, line in enumerate(inp.splitlines()):
    for x, cost in enumerate(map(int, line)):
        grid[x, y] = cost
        dist[x, y] = INF

dist[0, 0] = 0

mx = my = inp.count("\n")
mx += 1
my += 1
# horiz
for dy in range(1, 5):
    for x in range(mx):
        for y in range(my * dy, my * (dy + 1)):
            grid[x, y] = (grid[x, y - my]) % 9 + 1
            dist[x, y] = INF

# vert
for dx in range(1, 5):
    for y in range(my):
        for x in range(mx * dx, mx * (dx + 1)):
            grid[x, y] = (grid[x - mx, y]) % 9 + 1
            dist[x, y] = INF

# rest
for dx in range(1, 5):
    for dy in range(1, 5):
        for x in range(mx * dx, mx * (dx + 1)):
            for y in range(my * dy, my * (dy + 1)):
                grid[x, y] = (grid[x, y - my]) % 9 + 1
                dist[x, y] = INF

unvisited = [(0, (0, 0))]
while unvisited:
    dst, curr = heapq.heappop(unvisited)
    for nxt in adj(curr):
        try:
            cost = grid[nxt]
        except KeyError:
            continue
        d = dist[curr] + cost
        if d < dist[nxt]:
            dist[nxt] = d
            heapq.heappush(unvisited, (d, nxt))

print(dist[max(grid)])
