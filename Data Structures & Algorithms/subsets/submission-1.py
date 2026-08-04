class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        for i in range(2 ** len(nums)):
            subset = [nums[j] for j in range(len(nums)) if i & (1 << j)]
            ret.append(subset)

        return ret



        