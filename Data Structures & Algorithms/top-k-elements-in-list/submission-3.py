class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countFreq = {}

        for num in nums:
            countFreq[num] = 1 + countFreq.get(num, 0)
        
        arr = []

        for num, count in countFreq.items():
            arr.append([count, num])
        
        arr.sort()

        res = []

        for i in range(0, k):
            res.append(arr.pop()[1])
        
        return res

