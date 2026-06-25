
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # write all occurances into a hashmap
        count = Counter(tasks)
        heap = [-x for x in count.values()] # max heap
        heapq.heapify(heap)

        queue = deque() # pairs of [-count, idleTime]
        time = 0

        while heap or queue:
            time += 1
            if heap:
                c = 1 + heapq.heappop(heap)
                if c:
                    queue.append([c, time + n])
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
        return time