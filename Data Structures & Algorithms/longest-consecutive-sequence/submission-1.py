class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        output = 0
        nums_set = set(nums)
        visited_nums = set()

        for i in range(len(nums)):
            if nums[i] -1 not in nums_set and nums[i] not in visited_nums:
                max_con_seq = 1
                num = nums[i]
                while (num + 1 in nums_set):
                    max_con_seq += 1
                    num = num+1
                    visited_nums.add(num)
                output = max(output, max_con_seq)
        return output

        