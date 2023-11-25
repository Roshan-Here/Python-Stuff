# Given an integer array nums sorted in non-decreasing order, 
# remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same. 
# Then return the number of unique elements in nums.
# Consider the number of unique elements of nums to be k,
# to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
# The remaining elements of nums are not important as well as the size of nums.
# Return k.

class Solution(object):
    def removeDuplicates(self, nums):
        repelm = 0 #repeated element count
        for x in range(1,len(nums)):
            if nums[x] != nums[repelm]:
                repelm+=1
                nums[repelm] = nums[x]
        print(nums)
        return repelm+1
        #         # nums.pop(x)
        
        # # return repelm
        # count = 0
        # arr = []
        # for x in range(len(nums)):
        #     if x<(len(nums)-1) and nums[x]==nums[x+1]:
        #         continue
        #     else:
        #         arr.append(nums[x]) 
        #         count +=1
        # print(arr)
        # print(count)
                

# class Solution:
#     def removeDuplicates(self, nums):
#         # count = 0
#         # arr = []
#         # for x in range(len(nums)):
#         #     if x<(len(nums)-1) and nums[x]==nums[x+1]:
#         #         continue
#         #     else:
#         #         nums[count] = nums[x] 
#         #         count +=1
#         # print(nums)

#         j = 0
#         for x in range(1,len(nums)):
#             if nums[x] != nums[j]:
#                 j+=1
#                 nums[j]=nums[x]
#         print(nums)
#         return j+1

nums = [0,0,1,1,1,2,2,3,3,4]
x = Solution()
print(x.removeDuplicates(nums))