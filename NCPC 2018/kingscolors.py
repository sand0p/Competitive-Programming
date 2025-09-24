from math import comb

n, k = map(int, input().split())
mod = 1_000_000_007
print(sum((pow(-1, i, mod) * comb(k, i) * (k - i) * (k - i - 1) ** (n - 1)) % mod for i in range(k - 1)) % mod)
