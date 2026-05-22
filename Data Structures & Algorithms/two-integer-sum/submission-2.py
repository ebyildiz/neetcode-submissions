class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_set = set(nums)
        for i in range(len(nums)):
            if ((target-nums[i]) in my_set):
                idx = nums.index(target-nums[i])
                if i!=idx:
                    return sorted([i, idx])


            

        