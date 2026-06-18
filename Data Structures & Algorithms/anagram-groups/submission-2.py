class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_mapping = {}
        output = []
        for i in range(len(strs)):
            sorted_str = "".join(sorted(strs[i]))
            if sorted_str in dict_mapping:
                output[dict_mapping[sorted_str]].append(strs[i])
            else:
                output.append([strs[i]])
                dict_mapping[sorted_str] = len(output) - 1
        return output
                