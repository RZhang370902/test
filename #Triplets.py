#Triplets

res = []
nums = [-2,7,-8,-8,10,-5,-5,-5,-5,-5,-5,-8,-8,-8,-8,-8]

for I in range(0, len(nums) - 2, 1):
        for j in range(I + 1, len(nums) - 1, 1):
            for k in range(j + 1, len(nums), 1):
                if nums[I] + nums[j] + nums[k] == 0:
                    res.append([nums[I], nums[j], nums[k]])
print(res)

res_2 = []
nums.sort()

for i in range(0, len(nums) - 2, 1):
    if(i>0 and nums[i]==nums[i-1]): continue

    l = i + 1
    r = len(nums) - 1

    while (l<r):
        while (nums[i]==nums[l]):
            l+=1
        while (l<r):
            sum = nums[i] + nums[l] + nums[r]
            if sum < 0:
                l+=1
            elif sum > 0:
                r-=1
            else:
                res_2.append([nums[i], nums[l], nums[r]])
                l+=1


print(res_2)
