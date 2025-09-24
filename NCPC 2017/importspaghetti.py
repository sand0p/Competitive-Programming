from collections import deque

N = int(input())
nodes = input().split()
G = {}

for _ in range(N):
    node, k = input().split()
    children = []
    for _ in range(int(k)):
        tmp_children = input().split(", ")
        tmp_children[0] = tmp_children[0].split()[1]
        children += tmp_children
    G[node] = set(children)


def cycle_detect(node):
    visited = set()
    Q = deque()
    Q.append([node])
    prev = {n: n for n in G}
    visited = set()
    res = []
    while Q:
        path_to_node = Q.popleft()
        if path_to_node[-1] != node:
            visited.add(path_to_node[-1])
        for neigh in G[path_to_node[-1]]:
            if neigh in visited:
                continue
            if neigh == node:  # Back where we started
                return path_to_node
            Q.append(path_to_node + [neigh])
            visited.add(neigh)
    return res


shortest = float("inf")
best = []
for node in nodes:
    cyc = cycle_detect(node)
    if cyc and len(cyc) < shortest:
        best = cyc
        shortest = len(best)

if best:
    print(*best)
else:
    print("SHIP IT")
