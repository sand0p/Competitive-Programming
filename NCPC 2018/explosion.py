a, b, d = map(int, input().split())
our = list(map(int, input().split()))
opp = list(map(int, input().split()))

D = {}


def r(d, us, op):
    us.sort()
    op.sort()
    c = sum([e > 0 for e in us + op])
    if sum(op) > d:
        D[tuple(us + op)] = 0
        return 0
    if d > sum(us) + sum(op):
        D[tuple(us + op)] = 1
        return 1
    if d == 0 or c == 0:
        if sum(op) == 0:
            D[tuple(us + op)] = 1
            return 1
        else:
            D[tuple(us + op)] = 0
            return 0

    tot = 0

    for i in range(a):
        if us[i] == 0:
            continue
        new_us = us.copy()
        new_us[i] -= 1
        new_us.sort()
        if tuple(new_us + op) in D:
            tot += (1 / c) * D[tuple(new_us + op)]
        else:
            tot += (1 / c) * r(d - 1, new_us, op)

    for i in range(b):
        if op[i] == 0:
            continue
        new_op = op.copy()
        new_op[i] -= 1
        new_op.sort()
        if tuple(us + new_op) in D:
            tot += (1 / c) * D[tuple(us + new_op)]
        else:
            tot += (1 / c) * r(d - 1, us, new_op)

    D[tuple(us + op)] = tot
    return tot


print(r(d, our, opp))
