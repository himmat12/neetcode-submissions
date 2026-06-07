class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        try:    
            
            numFreq: dict = {}
            for num in nums:
                if numFreq.get(num) is not None:
                    numFreq[num] = numFreq.get(num) + 1
                else:
                    numFreq[num] = 1

            print(numFreq)

            for freq in numFreq:
                freqValue = numFreq.get(freq)
                if freqValue > 1:
                    return True
            return False     

        except Exception as e:
            print(e)
        