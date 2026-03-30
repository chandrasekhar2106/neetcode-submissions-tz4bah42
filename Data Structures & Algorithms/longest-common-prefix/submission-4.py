class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        if len(strs) < 1:
            return result
        n = len(strs[0])
        for i in range(1, len(strs)):
            if len(strs[i]) < n:
                n = len(strs[i])
            
        for i in range(n):
            tem_result = strs[0][:i+1]
            is_common = True
            for j in range(1, len(strs)):
                if strs[j][:i+1] != tem_result:
                    is_common=False
                    break
            if is_common:
                result = tem_result
            else:
                break
        return result
                




        