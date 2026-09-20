class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []
        for c in s:
            if stack and c in mp: 
                if stack.pop() != mp[c]:
                    return False
            else:
                stack.append(c)
        
        return True if len(stack) == 0 else False
