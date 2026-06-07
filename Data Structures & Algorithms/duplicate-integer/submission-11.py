class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_frequency = {}

        for num in nums:
            if not nums_frequency.get(num):
                nums_frequency[num] = 1
            else:
                return True
        return False
