class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 1 or len (strs) > 1000:
            return []
        
        strCharFreq: dict = {}

        for strKey in strs:
            if len(strKey) < 0 or len(strKey) > 100:
                return []

            sortedStr: str = ''.join(sorted(strKey.lower()))
            strCharFreq[sortedStr] = []
        
        for strValue in strs:
            sortedStr: str = ''.join(sorted(strValue.lower()))

            if strCharFreq.get(sortedStr) is not None:
                strCharFreq[sortedStr].append(strValue)

        return list(strCharFreq.values())