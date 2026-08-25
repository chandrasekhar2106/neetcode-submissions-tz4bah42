class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        res[0] = 1
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]
        suff = 1
        for j in range(n-1, -1, -1):
            res[j] = res[j] * suff
            suff = suff * nums[j]
        return res

        
        