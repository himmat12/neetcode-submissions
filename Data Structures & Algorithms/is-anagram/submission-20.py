
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        alphabet_pos_counts = [0] * 26

        for char_s, char_t in zip(s,t):
            alphabet_pos_counts[ord(char_s) - ord('a')] += 1
            alphabet_pos_counts[ord(char_t) - ord('a')] -= 1

        for count in alphabet_pos_counts:
            if count != 0:
                return False
        
        return True