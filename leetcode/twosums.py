# https://leetcode.com/problems/two-sum/description/
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for idx1, num1 in enumerate(nums):
            for idx2, num2 in enumerate(nums):
                if idx1 == idx2: 
                    continue
                if num1 + num2 == target: 
                    return [idx1, idx2]

nums = [2,7,11,15]
target = 9

resolve = Solution()
print(resolve.twoSum(nums,target))