class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        min_val: int = -10000000
        max_val: int = 10000000
        
        indices: dict = {}

        for i, n in enumerate(nums):
            indices[n] = i
        
        for i, n in enumerate(nums):
            diff: int = target - nums[i]

            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]

        return []
