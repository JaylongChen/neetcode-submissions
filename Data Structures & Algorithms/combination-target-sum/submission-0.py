class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []

        def dfs(i, total):
            if i >= len(nums) or total > target:  # failure state
                return

            if total == target:                   # success
                result.append(subset.copy()) 
                return

            subset.append(nums[i])
            dfs(i, total + nums[i])

            subset.pop()
            dfs(i + 1, total)

        dfs(0, 0)

        return result