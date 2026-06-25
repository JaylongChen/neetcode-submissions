class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        arrays = [[] for i in range(len(nums) + 1)]
        [[0],[1],[3],[2]]
        for num in nums:
            if num in freq.keys():
                freq[num] += 1
            else:
                freq[num] = 1

        for num, count in freq.items():
            arrays[count].append(num)
        
        result = []
        for i in range(len(arrays) - 1, 0, -1):
            for num in arrays[i]:
                if len(result) == k:
                    break
                result.append(num)
                
        return result

