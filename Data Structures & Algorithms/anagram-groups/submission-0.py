class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return strs

        group_map = defaultdict(list)

        for s in strs:
            sorted_s = sorted(s)
            group_map[str(sorted_s)].append(s)

        ret = []
        for val in group_map.values():
            ret.append(val)

        return ret

        