s = input()

rank = 25
stars = 0
streak = 0

for c in s:
    if c == "W":
        stars += 1
        streak += 1

        if streak >= 3 and rank >= 6:
            stars += 1

        if rank >= 21:
            if stars > 2:
                rank -= 1
                stars -= 2
        elif rank >= 16:
            if stars > 3:
                rank -= 1
                stars -= 3
        elif rank >= 11:
            if stars > 4:
                rank -= 1
                stars -= 4
        elif rank >= 1:
            if stars > 5:
                rank -= 1
                stars -= 5

        if rank == 0:
            print("Legend")
            exit()
    if c == "L":
        streak = 0
        if rank < 21:
            stars -= 1
        if stars < 0 and rank <= 20:
            rank += 1
            if rank == 21:
                rank = 20
                stars = 0
            elif rank >= 16:
                stars = 2
            elif rank >= 11:
                stars = 3
            elif rank >= 1:
                stars = 4

print(rank)
