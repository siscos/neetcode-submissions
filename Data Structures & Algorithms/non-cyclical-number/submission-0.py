class Solution:
    def _calculate(self, n: int) -> int:
        ret = 0
        while n > 0:
            ret += (n % 10) ** 2
            n //= 10

        return ret

    def isHappy(self, n: int) -> bool:
        number_set = set()
        while True:
            n = self._calculate(n)
            if n == 1:
                return True
            elif n in number_set:
                return False
            else:
                number_set.add(n)

        