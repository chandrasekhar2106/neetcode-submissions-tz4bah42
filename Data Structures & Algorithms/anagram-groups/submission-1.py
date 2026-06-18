class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        index_seen = []
        output = []
        for i in range(len(strs)):
            if i in index_seen:
                continue
            j = i+1
            s= "".join(sorted(strs[i]))
            sub_list = [strs[i]]
            while(j < len(strs)):
                if "".join(sorted(strs[j])) == s:
                    index_seen.append(j)
                    sub_list.append(strs[j])
                j += 1
            output.append(sub_list)
        return output