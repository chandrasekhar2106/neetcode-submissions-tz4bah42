class Solution:
    def countSubstrings(self, s: str) -> int:
        output = 0
        for i in range(1, len(s)+1):
            for j in range(i):
                if s[j:i] == s[j:i][::-1]:
                    output += 1
        return output
                