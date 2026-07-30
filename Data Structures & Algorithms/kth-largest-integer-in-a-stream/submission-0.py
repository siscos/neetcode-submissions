class KthLargest:
    _heap: List[int]
    _k: int

    def __init__(self, k: int, nums: List[int]):
        self._heap = []
        self._k = k
        for num in nums:
            heapq.heappush(self._heap, num)
            if len(self._heap) > k:
                heapq.heappop(self._heap)

    def add(self, val: int) -> int:
        heapq.heappush(self._heap, val)
        if len(self._heap) > self._k:
            heapq.heappop(self._heap)

        return self._heap[0]
