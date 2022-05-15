# potential_pairs lists each potential pair and its profit
def match(potential_pairs):
    # set of all queuers involved
    queuer = set()
    for i in potential_pairs:
        queuer = queuer.union(i[0])
    # all combinations of potential pairs
    import itertools
    comb = list(itertools.product([0, 1], repeat=len(potential_pairs)))
    # rule out combinations that involve any queuer multiple times
    comb_rule1 = []
    for j in comb:
        unmatched_queuer = queuer.copy()
        good = 1
        for k in range(len(j)):
            if j[k]:
                try:
                    for m in potential_pairs[k][0]:
                        unmatched_queuer.remove(m)
                except:
                    good = 0
                    break
        if good:
            comb_rule1.append(j)           
    # rule out combinations where there could have existed some additional pair that would not involve any queuer multiple times
    # e.g. if there are (1,1) and (1,0), then rule out (1,0)
    comb_rule2 = comb_rule1.copy()
    bad_index = []
    for n in range(len(comb_rule1)-1):
        if n not in bad_index:
            for p in range(n+1,len(comb_rule1)):
                diff = set()
                for q in range(len(potential_pairs)):
                    diff.add(comb_rule1[n][q]-comb_rule1[p][q])
                if diff == {0,-1}:
                    comb_rule2.remove(comb_rule1[n])
                    break
                elif diff == {0,1}:
                    comb_rule2.remove(comb_rule1[p])
                    bad_index.append(p)
    # find the combination(s) that yield maximum profit
    max_profit = 0
    result = []
    for r in comb_rule2:
        profit = 0
        for s in range(len(potential_pairs)):
            if r[s]:
                profit += potential_pairs[s][1]
        if profit > max_profit:
            max_profit = profit
            result = [r]
        elif profit == max_profit:
            result.append(r)
    return result
# demo
# 'a', 'b', 'c', 'd' are queuers. The numbers are profits.
potential_pairs = [[{'a','b'},1],[{'a','c'},2],[{'a','d'},1],[{'b','c'},1]]
print(match(potential_pairs))
print("0 for not trade, 1 for trade. Each number in order corresponds to a potential pair.")
