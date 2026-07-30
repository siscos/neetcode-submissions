class KthLargest:
    _min_heap: List[int]
    _k: int

    def __init__(self, k: int, nums: List[int]):
        self._min_heap = nums
        self._k = k
        heapq.heapify(self._min_heap)
        while len(self._min_heap) > self._k:
            heapq.heappop(self._min_heap)


    def add(self, val: int) -> int:
        heapq.heappush(self._min_heap, val)
        if len(self._min_heap) > self._k:
            heapq.heappop(self._min_heap)

        return self._min_heap[0]
