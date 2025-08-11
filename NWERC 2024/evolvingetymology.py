n, p = map(int, input().split())
w = input()
for i in range(n):
    indx = (i * pow(2, p, n)) % n
    print(end=w[indx])
print()