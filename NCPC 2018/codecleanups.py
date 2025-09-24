n = int(input())
A = list(map(int, input().split()))
res = 0
prev = []
indx = 0

for i in range(A[0], 366):
    if A[indx] == i:
        prev.append(A[indx])
        indx = min(n - 1, indx + 1)
    prev_n = [(i + 1) - e for e in prev]
    if sum(prev_n) < 20:
        continue
    else:
        # Cutting
        prev = []
        res += 1
if prev:
    res += 1
print(res)
