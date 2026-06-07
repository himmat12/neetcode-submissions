class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        sublist = []
        sorted_strs_dict = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))
            
            if not sorted_strs_dict.get(sorted_s):
                sorted_strs_dict[sorted_s] = [s]
            else:
                sorted_strs_dict.get(sorted_s).append(s)
        
        for item in sorted_strs_dict.items():
            sublist.append(item[1])
        
        return sublist


