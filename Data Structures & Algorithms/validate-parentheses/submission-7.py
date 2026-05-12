class Solution:
    def isValid(self, s: str) -> bool:
        map_list = []
        validMap = {
            ']': '[',
            '}': '{',
            ')': '(',
        }

        if len(s) % 2 != 0:
            return False
        for v in s:
            if v in validMap:
                if len(map_list) < 1:
                    return False
                popped_one = map_list.pop()
                if validMap[v] != popped_one:
                    return False   
            else:
                map_list.append(v)
        return len(map_list) == 0
