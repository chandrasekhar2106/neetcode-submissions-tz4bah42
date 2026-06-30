class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)
        output = [0] * k
        for num in nums:
            count_map[num] += 1
        
        sorted_ele = list(count_map.values())
        sorted_ele.sort(reverse=True)
        i = 0
        for key, value in count_map.items():
            if value in sorted_ele[:k]:
                output[i] = key
                i += 1
        return output



        
        