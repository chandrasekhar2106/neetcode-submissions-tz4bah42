class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        index = -1
        for i in range(len(operations)):
            if operations[i] == '+':
                result.append(result[index] + result[index-1])
            elif operations[i] == 'C':
                result.pop()
                index -= 1
                continue
            elif operations[i] == 'D':
                result.append(2 * result[index])                
            else:
                result.append(int(operations[i]))
            index += 1
        res = 0
        for val in result:
            res += val
        return res