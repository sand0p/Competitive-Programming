N = int(input())

input_list = [input().split() for _ in range(N)]

first_sorted = [(float(x[1]), x[0]) for x in input_list]
other_sorted = [(float(x[2]), x[0]) for x in input_list]

first_sorted.sort()
other_sorted.sort()

best_time = float("inf")
best_list = []

for time1, name1 in first_sorted:
    temp_best_list = [(time1, name1)]
    i = 0
    while len(temp_best_list) < 4:
        (time2, name2) = other_sorted[i]
        if name2 != name1:
            temp_best_list.append((time2, name2))
        i += 1
    temp_best_time = sum(x[0] for x in temp_best_list)
    if temp_best_time < best_time:
        best_time = temp_best_time
        best_list = temp_best_list

print(best_time)
for x in best_list:
    print(x[1])
