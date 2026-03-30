class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for s in strs:
            key = "".join(sorted(s))
            value = group.get(key, [])
            value.append(s)
            group[key] = value
        return list(group.values())
        