from math import log2


def phi(n: int) -> int:
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n = n // p
            result = result * (1.0 - (1.0 / float(p)))
        p = p + 1

    if n > 1:
        result -= result // n
    return int(result)


n, m = [int(x) for x in input().split()]

if m == 1:
    print(0)
    exit()

if n == 1:
    print(1)
    exit()

def f(n):
    if n == 1:
        return 1
    return pow(n, f(n - 1))

if n <= 5:
    print(pow(n, f(n - 1), m))
    exit()

theta_m = int(log2(m))

moduli = [m]
temp_phi = phi(m)

for i in range(1, theta_m):
    moduli.append(temp_phi)
    temp_phi = phi(temp_phi)

temp_exp = max(n - theta_m, 1)
temp_base = max(n - theta_m, 1)

index_corrector = theta_m - min(theta_m, n - 1)

for j in range(1, min(n, theta_m + 1)):
    temp_base += 1
    temp_exp = moduli[-j - index_corrector] + pow(temp_base, temp_exp, moduli[-j - index_corrector])
    
answer = temp_exp % m
print(answer)
