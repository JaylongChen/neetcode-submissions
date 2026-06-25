class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1 * x for x in stones]
        heapq.heapify(heap)

        while len(heap) > 1:

            heapq.heappush(heap, heapq.heappop(heap) - heapq.heappop(heap))

        if heap:
            return -1 * heap[0]
        else:
            return 0