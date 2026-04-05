class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, len_w1 = 0, len(word1)
        j, len_w2 = 0, len(word2)
        output = ""
        while(i < len_w1 and j < len_w2):
            output += word1[i] + word2[j]
            i += 1
            j += 1
        
        if (i < len_w1):
            output += word1[i:]
        elif (j < len_w2):
            output += word2[j:]
        return output