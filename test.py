# def SortList(nums):
#     max = 0
#     if len(nums) == 1:
#         return nums[0]
#     for i in range(len(nums)-1):
#         if nums.count(nums[i]) == nums.count(nums[i+1]):
#             pass
#         elif nums.count(nums[i]) > nums.count(nums[i+1]):
#             print(max)
#             max = nums[i]
#         else:
#             max = nums[i+1]
#     return max

# the above one is exceed the time limit

def majorityElement(nums):
    count = {}
    res , maxcount = 0 , 0
    for i in nums:
        count[i] = 1 + count.get(i,0)
        if count[i] > maxcount:
            res = i
            maxcount = count[i]
    return res 