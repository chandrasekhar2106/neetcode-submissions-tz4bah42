class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_map = {}

        for i in range(len(s)):
            char_map[s[i]] = char_map.get(s[i], 0) + 1
            char_map[t[i]] = char_map.get(t[i], 0) - 1

        for k, v in char_map.items():
            if v != 0:
                return False
        return True