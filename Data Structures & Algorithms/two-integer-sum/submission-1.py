class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums = {}
        for i, current_num in enumerate(nums):
            missing_num = target - current_num
            if missing_num in seen_nums:
                return [seen_nums[missing_num], i]
            seen_nums[current_num] = i