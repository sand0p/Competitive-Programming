n, ships = map(int, input().split())
sunk = 0


def shoot(x, y):
    global sunk
    print(x, y)
    resp = input()
    sunk += resp == "sunk"
    if sunk == ships:
        exit()
    return resp


def cross(x, y):
    global sunk
    global ships
    for dx in range(max(1, x - 4), min(n + 1, x + 5)):
        shoot(dx, y)
    for dy in range(max(1, y - 4), min(n + 1, y + 5)):
        shoot(x, dy)
    return


for y in range(1, n + 1):
    for x in range(1 + (y - 1) % 5, n + 1, 5):
        resp = shoot(x, y)
        if resp == "hit":
            cross(x, y)
