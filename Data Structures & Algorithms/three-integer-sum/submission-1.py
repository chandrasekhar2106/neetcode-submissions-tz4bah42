class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # -4, -1, -1, 0, 1, 2
        nums.sort()
        i, j, k = 0, 0, 0

        result = []


        for i in range(len(nums)):
            j, k = i+1, len(nums)-1
            while j < k:
                if -nums[i] == nums[j] + nums[k]:
                    if [nums[i], nums[j], nums[k]] not in result:
                        result.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                elif -nums[i] < nums[j] + nums[k]:
                    k -= 1
                else:
                    j += 1
        return result 