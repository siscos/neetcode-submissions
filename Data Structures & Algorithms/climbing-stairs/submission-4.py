from functools import cache

class Solution:
    @cache
    def _backtracking(self, step: int, n: int) -> int:
        if step > n:
            return 0
        elif step == n:
            return 1

        
        return self._backtracking(step + 1, n) + self._backtracking(step + 2, n)

    def climbStairs(self, n: int) -> int:
        self._cache = [-1] * (n + 1)
        return self._backtracking(0, n)
        