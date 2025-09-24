n, p = map(int, input().split())

f = [0] * (n + 1)
f[1] = p / (n + 1)
res = f[1]
for x in range(1, n):
    f[x + 1] = f[x] * ((x + 1) / x) * ((n + x + 1 - p) / (n + x + 1))
    res = max(res, f[x + 1])
print(res)