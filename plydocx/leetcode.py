
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        PrevMap = dict()
        for i, val in enumerate(nums):
            # i:index, val: index-item
            # print(i,val)
            print(PrevMap)
            diff = target - val
            if diff in PrevMap:
                return [PrevMap[diff],i]
            PrevMap[val] = i
            





        # i = 0
        # y = 0
        # arr = []
        # for x in nums:
        #     if i>nums.index(x):
        #         break
        #     else:
        #         i+=1
        #         arr.append(nums[i])
        #     # print(x)
        #     print(x,nums[i])
        #     if x + arr[i] == target:
        #         print("hello")
        #         j = nums.index(x)
        #         return [j,i]
        # for x in nums:
        #     # if i>len(nums):
        #     #     break
        #     # else:
        #     #     i+=1
        #     print(nums[i])
            # if x + nums[0] == target:
            #     return [nums.index(x),i]

        # for x in range(len(nums)):
        #     if i>nums.index(nums[x]):
        #         break
        #     else:
        #         i+=1
        #         arr.append(nums[i])
        #     print(arr)
        #     print(nums)
        #     if nums[x] + arr[y] == target:
        #         return [x] 

        # for x in range(len(nums)):
        #     y = x+1
        #     # print(len(nums))
        #     if y>=len(nums):
        #         break
        #     else:
        #         arr.append(nums[y])
        #     if nums[x] + arr[x] == target:
        #         print("hello")
        #         j = x+1
        #         return [x,j]
        # print(nums,arr)


        #     # x = 1,2,3
        #     y = nums[x+1]
        #     print(nums[x])
            
        
        #     y = x+1
        #     if x == y:
        #         break
        #     else:
        #         if nums[x] + nums[y] == target:
        #             return list(nums[x],nums[y])



x = Solution()
wow = [2,7,11,15]
target = 17
print(x.twoSum(wow,target))