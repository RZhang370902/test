def twoCitySchedCost(list):

    diffs = []

    for individual in list:
        cityA, cityB = individual
        diffs.append([cityB - cityA, cityA, cityB])

    diffs.sort()

    res_1 = 0
    res_2 = 0
    res_3 = 0

    for i in range(len(diffs)//2):
        res_1 += diffs[i][0]
    
    for i in range(len(diffs)):
        res_2 += diffs[i][1]

    res_3 = res_1 + res_2
    return res_3

costs = [[10,20],[30,200],[400,50],[30,20]]
result = twoCitySchedCost(costs)
print(result)