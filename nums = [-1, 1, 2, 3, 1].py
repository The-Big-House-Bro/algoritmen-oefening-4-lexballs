nums = [-1, 1, 2, 3, 1]
target = 2

def counttargetpairs(nums, target):
    answer = 0
    n = len(nums)
    
    for i in range (n):
        for j in range(i + 1, n):
            if nums[1] + nums[j] < target:
                answer += 1
                
    print(answer)
counttargetpairs(nums, target)