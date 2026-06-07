class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sortedS: str = ''.join(sorted(s.lower()))
        sortedT: str = ''.join(sorted(t.lower()))

        if sortedS != sortedT:
            return False

        # sCharFreq: dict = {}
        # tCharFreq: dict = {}

        # for char in lowerS:
        #     if sCharFreq.get(char) is not None:
        #         sCharFreq[char] = sCharFreq.get(char) + 1
        #     else:
        #         sCharFreq[char] = 1

        # for char in lowerT:
        #     if tCharFreq.get(char) is not None:
        #         tCharFreq[char] = tCharFreq.get(char) + 1
        #     else:
        #         tCharFreq[char] = 1
        

        # for sChar in sCharFreq:
        #     print (sChar)
        #     if tCharFreq.get(sChar) is None:
        #         return False
            
        #     if tCharFreq.get(sChar) != sCharFreq.get(sChar):
        #         return False
            
        return True
