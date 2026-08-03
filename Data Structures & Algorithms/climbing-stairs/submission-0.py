class Solution:
    def _backtracking(self, step: int, n: int) -> int:
        if step > n:
            return 0
        elif step == n:
            return 1

        if self._cache[step] != -1:
            return self._cache[step]

        self._cache[step] = self._backtracking(step + 1, n) + self._backtracking(step + 2, n)
        return self._cache[step]

    def climbStairs(self, n: int) -> int:
        self._cache = [-1] * (n + 1)
        return self._backtracking(0, n)
        