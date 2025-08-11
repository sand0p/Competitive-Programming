days = [input() for _ in range(7)]
d, h = map(int, input().split())

best = 0
for n in range(1 << 7):
    if n.bit_count() != d:
        continue
    dz = []
    for i in range(7):
        if n & 1 << i:
            dz.append(days[i])

    hours = [sum(e[i].count(".") for e in dz) for i in range(24)]
    hours.sort(reverse=1)
    tot_free = sum(hours[:h])
    best = max(best, tot_free / (d * h))

print(best)