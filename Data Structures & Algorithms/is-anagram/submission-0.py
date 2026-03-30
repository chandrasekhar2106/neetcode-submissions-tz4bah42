class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_index_map = {}
        for i, char in enumerate(t):
            char_index_map[char] = char_index_map.get(char, 0) + 1
        
        for char in s:
            if not char in char_index_map:
                return False
            char_index_map[char] -= 1
            if char_index_map[char] == 0:
                char_index_map.pop(char) 
        if char_index_map:
            return False
        return True