class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k] # split the first k
        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]: # heap[0] is the kth largest
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        
        return heap[0]


        