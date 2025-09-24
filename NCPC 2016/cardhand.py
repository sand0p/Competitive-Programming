from itertools import permutations
from bisect import bisect_left

def lis(S):
    prev, res = [], []
    for i, v in enumerate(S):
        el = (v, i)
        # v + 1 for non-decreasing
        j = bisect_left(res, (v, 0))
        if j == len(res):
            res.append(el)
        else:
            res[j] = el
        prev.append(0 if j == 0 else res[j - 1][1])
    ans = []
    cur = res[-1][1]
    for _ in range(len(res)):
        ans.append(cur)
        cur = prev[cur]
    return len(ans)


def calc(cards, ordering):
    n = len(cards)
    res = [ordering.index(e) for e in cards]
    return n - lis(res)


suits = list("shdc")
ting = list("123456789TJQKA")
suit_perms = permutations(suits)
all_orders = []
for perm in suit_perms:
    for rev in range(0, 1 << 4):
        loc_res = []
        for i in range(4):
            s = perm[i]
            if rev & (1 << i):
                loc = ting[::-1]
            else:
                loc = ting[:]
            for c in loc:
                loc_res.append(c + s)
        all_orders.append(loc_res)
n = int(input())
cards = input().split()

print(min(calc(cards, order) for order in all_orders))
