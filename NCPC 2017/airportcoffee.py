import bisect

l, a, b, t, r = map(int, input().split())
n = int(input())

if n == 0:
    print(0)
    exit()

stand = list(map(int, input().split()))
stand.append(l)
memo = [(0, -1) for _ in range(n + 1)]


for i in range(n - 1, -1, -1):
    coffee_stand = stand[i]
    coffee_start = a * t + coffee_stand
    coffee_end = b * r + coffee_start
    tries = []
    mn = i + 1

    if stand[mn] <= coffee_start:
        time = (stand[mn] - coffee_stand) / a
        tries.append((mn, time))

    mn = bisect.bisect_right(stand, coffee_end) - 1

    if coffee_start < stand[mn] <= coffee_end:
        time = t + (stand[mn] - coffee_start) / b
        tries.append((mn, time))

    mn += 1

    if mn <= n and coffee_end < stand[mn]:
        time = t + r + (stand[mn] - coffee_end) / a
        tries.append((mn, time))

    best_time = float("inf")
    best_next = -1

    for ind, time in tries:
        rest_time, _ = memo[ind]
        if time + rest_time < best_time:
            best_time = time + rest_time
            best_next = ind

    memo[i] = best_time, best_next

res = [0]
on = memo[0][1]

while on != -1 and on != n:
    res.append(on)
    on = memo[on][1]

print(len(res))
print(*res)
