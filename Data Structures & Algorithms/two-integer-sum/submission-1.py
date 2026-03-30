class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force
        n = len(nums)
        mapping = {}
        for i in range(n):
            if nums[i] in mapping:
                return [mapping[nums[i]], i]
            mapping[target-nums[i]] = i
        
        