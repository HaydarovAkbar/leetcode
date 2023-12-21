class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        '''This is a solution for the problem'''
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        return []
