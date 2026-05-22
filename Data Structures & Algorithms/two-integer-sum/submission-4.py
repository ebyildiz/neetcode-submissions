class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        snums = set(nums)
        for i in range(len(nums)):
            if target - nums[i] in snums:
                idx = nums.index(target-nums[i])
                if idx!=i:
                 return sorted([idx, i])


