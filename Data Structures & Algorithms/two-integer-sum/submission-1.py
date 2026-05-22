class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            search = target-nums[i]
            if search not in nums:
                continue
            searched = nums.index(search)
            if searched == i:
                continue
            return sorted([i, nums.index(search)])


            

        