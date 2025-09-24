import heapq as pq

inf = float("inf")

h, w = map(int, input().split())

lake = [list(map(int, input().split())) for _ in range(h)]
pump = tuple(map(int, input().split()))
res = lake[pump[0] - 1][pump[1] - 1]
max_allowed = res

Q = []
pq.heappush(Q, (-inf, (pump[0] - 1, pump[1] - 1)))
visited = set()

while Q:
    cap_to_reach, node_at = pq.heappop(Q)
    if node_at in visited:
        continue
    visited.add(node_at)
    if cap_to_reach != -inf:
        res += cap_to_reach
    y, x = node_at
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if (dx, dy) == (0, 0) or (y + dy, x + dx) in visited:
                continue
            if 0 <= x + dx < w and 0 <= y + dy < h:
                edge_cap = max(cap_to_reach, lake[y + dy][x + dx], max_allowed)
                if edge_cap < 0:
                    pq.heappush(Q, (edge_cap, (y + dy, x + dx)))
print(-res)
