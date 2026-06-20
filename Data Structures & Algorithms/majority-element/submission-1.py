class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        count = 1
        for num in nums:
            if majority == num:
                count += 1
            else:
                if count == 1:
                    majority = num
                else:
                    count -= 1
        return majority