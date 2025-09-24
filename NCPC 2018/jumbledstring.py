a, b, c, d = map(int, input().split())

temp_n = (1 + 8 * a) ** 0.5
temp_m = (1 + 8 * d) ** 0.5

n = 1 + (temp_n - 1) // 2
m = 1 + (temp_m - 1) // 2

st = "impossible"

if (
    abs(temp_n - round(temp_n)) < 1e-6
    and abs(temp_m - round(temp_m)) < 1e-6
    and b + c == m * n
):
    yahoo = m - c // n - 1
    st = int(c // n) * "1" + int(n - c % n) * "0"
    if c % n != 0 or c == 0:
        st += "1"
    else:
        yahoo = m - c // n
    st += int(c % n) * "0" + int(yahoo) * "1"
elif a + b + c == 0 and abs(temp_m - round(temp_m)) < 1e-6:
    st = int(m) * "1"
elif b + c + d == 0 and abs(temp_n - round(temp_n)) < 1e-6:
    st = int(n) * "0"

print(st)
