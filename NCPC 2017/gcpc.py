teams, haps = map(int, input().split())
better_than_us = set()

score = [(0, 0)] * (teams + 1)  # (probs,time penalty)

for _ in range(haps):
    team, tp = map(int, input().split())
    score[team] = (score[team][0] + 1, score[team][1] + tp)

    if score[team][0] > score[1][0] or (score[team][0] == score[1][0] and score[team][1] < score[1][1]):
        better_than_us.add(team)
    if team == 1:
        new_set = set()
        for e in better_than_us:
            if score[e][0] > score[1][0] or (score[e][0] == score[1][0] and score[e][1] < score[1][1]):
                new_set.add(e)
        better_than_us = new_set.copy()
    print(1 + len(better_than_us))