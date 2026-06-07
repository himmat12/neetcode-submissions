class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        nums_frequency = {}

        for num in sorted_nums:
            if not nums_frequency.get(num):
                nums_frequency[num] = 1
            else:
                return True
        
        return False
        