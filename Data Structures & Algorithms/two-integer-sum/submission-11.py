class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            indeces = []
            for index, element in enumerate(nums):
                indeces.append(index)
            return indeces

        nums_freq = {}

        for i, num in enumerate(nums):
            nums_freq[num] = i
        
        for i in range(len(nums)):
            diff =  target - nums[i]

            if nums_freq.get(diff) and i != nums_freq.get(diff):
                return [i, nums_freq.get(diff)]
        

        