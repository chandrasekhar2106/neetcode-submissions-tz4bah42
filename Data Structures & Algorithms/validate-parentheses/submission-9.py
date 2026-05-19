class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        mapping = {
            "}": "{",
            ")": "(",
            "]" : "["
        }
        
        for c in s:
            if c in mapping and arr and mapping[c] in arr[-1]:
                arr.pop()
            else:
                arr.append(c)
        return True if len(arr) == 0 else False
