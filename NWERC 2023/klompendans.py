from collections import deque

n = int(input())
m1 = tuple(map(int, input().split()))
m2 = tuple(map(int, input().split()))


def swap(move):
    if move == m1:
        return m2
    return m1


def moves(y, x, move):
    dy, dx = move
    return [
        (y + dy, x + dx),
        (y - dy, x + dx),
        (y + dy, x - dx),
        (y - dy, x - dx),
        (y + dx, x + dy),
        (y - dx, x + dy),
        (y + dx, x - dy),
        (y - dx, x - dy),
    ]


res = set()
res.add((0, 0))


def check(move):
    global res
    visit_with_m1 = [[False] * n for _ in range(n)]
    visit_with_m2 = [[False] * n for _ in range(n)]
    Q = deque([(0, 0, move)])
    while Q:
        y, x, move = Q.popleft()
        for yy, xx in moves(y, x, move):
            if 0 <= yy < n and 0 <= xx < n:
                if move == m1:
                    if not visit_with_m1[yy][xx]:
                        res.add((yy, xx))
                        visit_with_m1[yy][xx] = True
                        Q.append((yy, xx, swap(move)))
                else:
                    if not visit_with_m2[yy][xx]:
                        res.add((yy, xx))
                        visit_with_m2[yy][xx] = True
                        Q.append((yy, xx, swap(move)))


check(m1)
check(m2)
print(len(res))
