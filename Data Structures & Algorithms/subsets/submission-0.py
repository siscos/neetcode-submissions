class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        for i in range(2 ** len(nums)):
            tmp = []
            for j in range(len(nums)):
                if i & 1 << j != 0:
                    tmp.append(nums[j])

            ret.append(tmp)

        return ret



        