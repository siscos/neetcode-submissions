class Solution:
    def _create_subset(self, index: int, nums: list[int], subset: list[list[int]]) -> None:
        if index >= len(nums):
            return

        new_subset = deepcopy(subset)
        for new in new_subset:
            new.append(nums[index])

        subset.extend(new_subset)
        self._create_subset(index + 1, nums, subset)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        self._create_subset(0, nums, ret)
        return ret




        