n = int(input())
names = [input() for _ in range(n)]
nms = []

for nm in names:
    indx = 0
    while nm[indx] not in "ASDFGHJKLQWERTYUIOPZXCVBNM":
        indx += 1
    nms.append((nm[indx:], nm))
nms.sort(key=lambda e: e[0])

for e in nms:
    print(e[1])
