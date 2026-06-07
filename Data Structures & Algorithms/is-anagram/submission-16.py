
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        s_char_freq = {}
        t_char_freq = {}

        for i in range(len(sorted_s)):
            s_char = sorted_s[i]
            t_char = sorted_t[i]

            if not s_char_freq.get(s_char):
                s_char_freq[s_char] =  1
            else:
                s_char_freq[s_char] = s_char_freq.get(s_char) + 1
                
            if not t_char_freq.get(t_char):
                t_char_freq[t_char] =  1
            else:
                t_char_freq[t_char] = t_char_freq.get(t_char) + 1
        
        if not s_char_freq.items() == t_char_freq.items():
            return False

        return True

        