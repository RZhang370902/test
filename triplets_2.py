def triple_search(list):
    res = []
    list.sort()

    for i in range(0, len(list) - 2, 1):
        if(i>0 and list[i]==list[i-1]): continue

        l = i + 1
        r = len(list) - 1

        #while (l<r):
        while (list[i]==list[l]):
                 l+=1
        while (l<r):
                sum = list[i] + list[l] + list[r]
                if sum < 0:
                    l+=1
                elif sum > 0:
                    r-=1
                else:
                    res.append([list[i], list[l], list[r]])
                    l+=1
    return res

nums = [-2,7,-8,-8,10,-5,-5,-5,-5,-5,-5,-8,-8,-8,-8,-8]

result = triple_search(nums)
print(result)