class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in nums:
            if (num - 1) not in numSet:
                currentLen = 0
                while (num + currentLen) in numSet:
                    currentLen += 1
                longest = max(currentLen, longest)
        return longest
        
        