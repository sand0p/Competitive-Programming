n = int(input())
p = list(map(int, input().split()))
p.sort(reverse=1)
tot = sum(p)

dp = [0] * (tot + 1)
dp[0] = 1
res = 0

for party in p:
    for j in range(tot, party - 1, -1):
        if j > tot - j and (j - party) <= tot - (j - party):
            res += dp[j - party]
        dp[j] += dp[j - party]

print(res)
