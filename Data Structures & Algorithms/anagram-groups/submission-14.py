class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_freq = defaultdict(list[str])
        
        for s in strs:
            char_count = [0] * 26
            for c in s:
                i = ord('a') - ord(c)
                char_count[i] += 1
            char_freq[tuple(char_count)].append(s)
        return list(char_freq.values())


