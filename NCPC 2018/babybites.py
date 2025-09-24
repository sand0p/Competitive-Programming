n = int(input())
liste = input().split()
sg = "something is fishy"
for i in range(1, n + 1):
    if str(i) != liste[i - 1] and liste[i - 1] != "mumble":
        break
else:
    sg = "makes sense"
print(sg)
