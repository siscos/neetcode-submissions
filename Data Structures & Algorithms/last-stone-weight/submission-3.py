from heapq import heapify, heappop, heappush

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        tmp = [-n for n in stones]

        heapify(tmp)
        while True:
            print(f'{tmp}')
            first = heappop(tmp)
            second = heappop(tmp)
            diff = -abs(first - second)
            if diff != 0: 
                heappush(tmp, diff)

            

            if len(tmp) == 1:
                return -tmp[0]
            elif len(tmp) == 0:
                return 0
