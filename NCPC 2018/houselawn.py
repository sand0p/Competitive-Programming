lawn, n = map(int, input().split())
cheapest = []
mn = float("inf")
week = 10_080

for _ in range(n):
    name, *line = input().split(",")
    price, cap, time, charge = map(int, line)
    # lawn_per_cycle=(cap * time) / lawn
    # cycle_per_day=(time + charge) / week
    t = (time / (time + charge)) * cap * week
    if t >= lawn:
        if price == mn:
            cheapest.append(name)
        elif price < mn:
            mn = price
            cheapest = [name]

if cheapest:
    for e in cheapest:
        print(e)
else:
    print("no such mower")
