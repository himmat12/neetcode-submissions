class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_freq = {}

        for i, num in enumerate(nums):
            nums_freq[num] = i
        
        for i in range(len(nums)):
            diff =  target - nums[i]

            if nums_freq.get(diff) and i != nums_freq.get(diff):
                return [i, nums_freq.get(diff)]
        

        return [0, 1]

        