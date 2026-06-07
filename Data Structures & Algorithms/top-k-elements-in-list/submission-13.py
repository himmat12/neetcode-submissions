class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_frequency = defaultdict(int)

        for num in nums:
            nums_frequency[num] += 1

        sorted_nums_frequency = dict(
            sorted(nums_frequency.items(), key=lambda item: item[1], reverse=True)
        )

        res = []

        n = len(nums)

        buckets = [[] for _ in range(n + 1) ]

        for num, freq in sorted_nums_frequency.items():
            buckets[freq].append(num)
        
        for i in range(n , 0, -1):
            if buckets[i]:
                for num in buckets[i]:
                    res.append(num)
                    if len(res) == k:
                        return res

        return res
