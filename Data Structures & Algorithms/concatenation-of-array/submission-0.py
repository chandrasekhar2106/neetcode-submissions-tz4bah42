class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0] * (2*n)
        for i, value in enumerate(nums):
            arr[i] = value
            arr[i+n] = value
        return arr
        