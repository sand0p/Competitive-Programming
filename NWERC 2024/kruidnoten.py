import heapq
n, m, k = map(int, input().split())

G = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    G[a].append((b, w))
    G[b].append((a, w))

nuts = [0] * (n + 1)
found_one = False
for _ in range(k):
    a, prob = input().split()
    nuts[int(a)] = float(prob)
    if float(prob) == 1:
        found_one = True

if not found_one:
    print("impossible")
    exit()


def dijk(orig):
    global G
    Q = [(0, orig)]
    dist = [float("inf")] * (n + 1)
    dist[orig] = 0
    visited = set()
    while Q:
        w, at = heapq.heappop(Q)
        if at in visited:
            continue
        visited.add(at)
        for neigh, dst in G[at]:
            if dist[at] + dst < dist[neigh]:
                dist[neigh] = dist[at] + dst
                heapq.heappush(Q, (dist[neigh], neigh))
    return dist


from_orig = dijk(1)
from_end = dijk(n)
tot_dists = []

for i in range(1, n + 1):
    if nuts[i]:
        tot_dists.append((from_end[i] + from_orig[i], nuts[i]))
tot_dists.sort()


res = 0
prob = 1
for dist, p in tot_dists:
    if dist == float("inf"):
        print("impossible")
        break
    res += dist * p * prob
    if p == 1:
        print(res)
        break
    prob *= 1 - p