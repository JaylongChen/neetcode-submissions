class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(i, subset):
            # base case
            if i == len(nums):
                # copy of subset
                result.append(subset[::])
                return
            
            # left sub branch | including nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # right sub branch | doesnt include nums[i]
            # since we pre sorted nums[], we will skip over duplicated number
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            backtrack(i + 1, subset)

        backtrack(0, [])

        return result
