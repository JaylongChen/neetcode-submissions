class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            x, y = point
            distances.append([(x ** 2 + y ** 2), point])

        heapq.heapify(distances)

        results = []
        for i in range(k):
            results.append(heapq.heappop(distances)[1])

        return results