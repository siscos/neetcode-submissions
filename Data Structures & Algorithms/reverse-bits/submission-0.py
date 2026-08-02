class Solution:
    def reverseBits(self, n: int) -> int:
        ret: int = 0
        for i in range(32):
            bi: int = 1
            bi <<= i

            if n & bi != 0:
                ret |= 1 << (31 - i) 

        return ret