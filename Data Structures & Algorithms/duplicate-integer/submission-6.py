class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_frequency = {}

        for num in nums:
            if not nums_frequency.get(num):
                nums_frequency[num] = 1
            else:
                nums_frequency[num] = nums_frequency.get(num) + 1

        for key, val in nums_frequency.items():
            if val > 1:
                return True
        return False
