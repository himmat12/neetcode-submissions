class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths differ, cannot be anagrams
        if len(s) != len(t):
            return False

        # Frequency array for 26 lowercase letters
        counts = [0] * 26

        # Count characters from s and t in one pass
        for cs, ct in zip(s, t):
            counts[ord(cs) - ord('a')] += 1
            counts[ord(ct) - ord('a')] -= 1

        # All counts must end up zero
        for c in counts:
            if c != 0:
                return False

        return True
