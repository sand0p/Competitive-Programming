a = int(input())
b = int(input())
l = []
if abs(b - a) == 180:
    l.append(180)

if abs(a - b) < 180:
    l.append(b - a)
else:
    if abs(a - 0) < abs(b - 0):
        if a > 180:
            a = 360 - a
        if b > 180:
            b = 360 - b
        l.append(-(a + b))
    else:
        if a > 180:
            a = 360 - a
        if b > 180:
            b = 360 - b
        l.append(a + b)
print(l[0])
