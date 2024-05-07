def two_sum(list,target):
    res = []
    i = 0
    for i in range(0,len(list)-1):
        for l in range(i+1,len(list)):
            if list[i] + list[l] == target:
                res.append([i,l])
    return res

def twoSum(list,target):

    map = {}
    res = []

    for i in range(0, len(list), 1):
        map[list[i]] = i

    for i in range(0, len(list), 1):
        difference = target - list[i]
        if difference in map:
            return([map[difference], i])
            #res.append([map[difference], i])
    #return res

def twoSumEn(list, target):

    seen = {}

    for i, num in enumerate(list):
        if target - num in seen:
            return([seen[target - num], i])
        elif num not in seen:
            seen[num] = i

nums = [1,8,11,2,7,15]
target = 9

result = two_sum(nums,target)
print(result)

result = twoSum(nums,target)
print(result)

result = twoSumEn(nums,target)
print(result)