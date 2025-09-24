n = int(input())
inf = float("inf")

cash = 100
prev = inf

for _ in range(n):
    now = int(input())
    if now > prev:
        cash += min(cash // prev, 100_000) * (now - prev)
    prev = now
print(cash)
