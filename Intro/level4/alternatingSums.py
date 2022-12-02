def solution(a):
    team1_wtd = [a[i] for i in range(0,len(a)) if i % 2 == 0]
    team2_wtd = [a[i] for i in range(0,len(a)) if i % 2 != 0]
    # edge case for empty t2
    if len(team2_wtd) == 0: team2_wtd.append(0)
    from functools import reduce
    return [reduce(lambda a,b: a+b, team1_wtd), reduce(lambda a,b: a+b, team2_wtd)]
