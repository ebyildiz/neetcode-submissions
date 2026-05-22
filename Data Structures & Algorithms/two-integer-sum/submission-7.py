class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappy = {}
        for i in range(len(nums)):
            other = target - nums[i]
            if other in mappy:
                return [mappy[other], i]
            mappy[nums[i]]=i
        
