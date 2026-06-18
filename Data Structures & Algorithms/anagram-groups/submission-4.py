class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_mapping = {}
        output = []
        for i in range(len(strs)):
            sorted_str = "".join(sorted(strs[i]))
            if sorted_str in dict_mapping:
                dict_mapping[sorted_str].append(strs[i])
            else:
                dict_mapping[sorted_str] = [strs[i]]
        
        return list(dict_mapping.values())
                