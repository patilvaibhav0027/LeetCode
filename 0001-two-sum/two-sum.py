class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        i = 0
        j = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums), 1):
                if target == (nums[i]+nums[j]):
                    return [i,j]