n, s = map(int, input().split())
chrg = list(map(int, input().split()))

if s == 1 or n == 1:
    print(1)
    exit()

chrg.sort()

# Two largest on outside facing out
tot = 2
chrg.pop()
chrg.pop()


def fits(k):
    res = 0

    mod_null = []
    mod_one = []
    mod_two = []

    for i in range(min(k, n - 2)):
        charger = chrg[i]
        md = charger % 3
        if md == 0:
            mod_null.append(charger)
        elif md == 1:
            mod_one.append(charger)
        else:
            mod_two.append(charger)

    mod_one = mod_one[::-1]
    mod_two = mod_two[::-1]

    # I
    for c in mod_null:
        res += c // 3

    # II
    while mod_one and mod_two:
        double = mod_one.pop() + mod_two.pop()
        res += double // 3

    # III
    while len(mod_one) >= 2:
        double = mod_one.pop() + mod_one.pop() + 1
        res += double // 3

    # IV
    while mod_two:
        double = mod_two.pop() + 1
        res += double // 3

    # V
    while mod_one:
        double = mod_one.pop() + 2
        res += double // 3

    return res


# Binary search on if we can fit n adaptors
high = n - 1
low = 0
mid = 0
while high - low > 1:
    mid = (high + low) >> 1
    chck = fits(mid)
    if chck > s - 2:
        high = mid
    else:
        low = mid
tot += low

print(tot)
