class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        mid = 0

        while low <= high:
            mid = (low + high)//2

            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return low 
    

        