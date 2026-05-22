class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_set = set(nums)
        index_dict = {value: idx for idx, value in enumerate(nums)}
        for i in range(len(nums)):
            if ((target-nums[i]) in my_set):
                idx = index_dict[target-nums[i]]
                if i!=idx:
                    return sorted([i, idx])


            

        