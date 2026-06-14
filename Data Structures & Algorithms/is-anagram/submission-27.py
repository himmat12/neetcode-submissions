class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_freq = defaultdict(int)

        for char_s, char_t in zip(s,t):
            char_freq[char_s] += 1
            char_freq[char_t] -= 1
        
        for count in char_freq.values():
            if count != 0:
                return False
        return True
        