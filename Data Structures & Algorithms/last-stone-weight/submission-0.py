class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1 * x for x in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            a = heapq.heappop(heap) # heaviest
            b = heapq.heappop(heap) # 2nd heaviest

            heapq.heappush(heap, a - b)

        if heap:
            return -1 * heap[0]
        else:
            return 0