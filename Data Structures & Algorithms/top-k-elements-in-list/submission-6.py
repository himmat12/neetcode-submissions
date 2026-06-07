class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_frequency = defaultdict(int)

        for num in nums:
            nums_frequency[num] += 1

        sorted_nums_frequency = dict(
            sorted(nums_frequency.items(), key=lambda item: item[1], reverse=True)
        )

        res = []

        i = 1
        for item in sorted_nums_frequency.items():
            if i <= k:
                res.append(item[0])
                i += 1
            else:
                break

        return res
