class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ret = []
        gotto = 1
        for n in digits[::-1]:
            print(f'{n=}, {gotto=}')
            if n + gotto >= 10:
                gotto = 1
                ret.append(0)
            else:
                ret.append(n + gotto)
                gotto = 0
        
        if gotto != 0:
            ret.append(gotto)
        
        return ret[::-1]