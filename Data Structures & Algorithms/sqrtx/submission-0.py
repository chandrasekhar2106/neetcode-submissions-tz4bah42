class Solution:
    def mySqrt(self, x: int) -> int:
        num = 0
        while(num ** 2 <= x):
            if (num ** 2 == x):
                return num
            else:
                num += 1
        return num-1