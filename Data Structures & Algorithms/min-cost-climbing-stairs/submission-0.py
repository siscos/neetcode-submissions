from functools import cache

class Solution:
    def _backtracking(self, step: int, cost: list[int]) -> int:
        len_cost = len(cost)
        if step >= len_cost:
            return 0

        if self._cache[step] != -1:
            return self._cache[step]

        self._cache[step] = cost[step] + min(self._backtracking(step + 1, cost), self._backtracking(step + 2, cost))
        return self._cache[step]


    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self._cache = [-1] * len(cost)
        return min(self._backtracking(0, cost), self._backtracking(1, cost))
        