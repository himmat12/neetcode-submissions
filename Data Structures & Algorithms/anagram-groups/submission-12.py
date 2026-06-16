class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_freq = defaultdict(list[str])

        for s in strs:
            sorted_str = "".join(sorted(s))
            str_freq[sorted_str].append(s)
        res = []
        for val in str_freq.values():
            res.append(val)
        return res

