class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_freq = defaultdict(int)

        for num in nums:
            num_freq[num] += 1
        
        for count in num_freq.values():
            if count > 1:
                return True
        return False
        