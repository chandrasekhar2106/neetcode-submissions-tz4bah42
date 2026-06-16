class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_mapping = {}
        for i in range(len(nums)):
            if nums[i] in nums_mapping:
                return [nums_mapping[nums[i]], i]
            nums_mapping[target-nums[i]] = i
        