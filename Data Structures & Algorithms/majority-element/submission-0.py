class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_map = {}

        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1

        max_val = 0; result = 0; 
        for key, value in count_map.items():
            if max_val < value:
                result = key
                max_val = value

        return result