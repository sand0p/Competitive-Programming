import heapq as pq

n = int(input())
A = list(map(int, input().split()))
A = [(e, e) for e in A]
pq.heapify(A)

ones = 0
while A and A[0][0] == 1:
    ones += 1
    pq.heappop(A)

for _ in range(ones):
    if len(A) > 1 and A[0][0] < 3:
        a, b = pq.heappop(A)
        pq.heappush(A, (a + 1, b))
    else:
        pq.heappush(A, (1, 1))

if len(A) > 1 and A[0][0] == 1:
    pq.heappop(A)
    a, b = pq.heappop(A)
    pq.heappush(A, (a + 1, b))

res = []
for b, a in A:
    s = "(" + str(a)
    s += "+1" * (b - a)
    s += ")"
    res.append(s)

print(*res, sep="*")