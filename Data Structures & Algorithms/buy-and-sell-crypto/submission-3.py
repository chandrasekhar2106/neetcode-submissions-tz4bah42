class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        end = 1
        ans = 0
        while (end < len(prices)):
            if prices[end] - prices[start] > ans:
                ans = prices[end] - prices[start]
            if prices[start] > prices[end]:
                start = end
            end += 1
        return ans