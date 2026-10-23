class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nos = {}

        for i, current_num in enumerate(nums):
            missing_no = target - current_num

            if missing_no in seen_nos:
                return [seen_nos[missing_no], i]
            
            seen_nos[current_num] = i