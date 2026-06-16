class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums_count = defaultdict(int)
        for num in nums:
            nums_count[num] += 1
        arr = []
        for num, count in nums_count.items():
            arr.append([count, num])
        
        arr.sort()
        res =[]
        while len(res) < k:
            res.append(arr.pop()[1])
        return res