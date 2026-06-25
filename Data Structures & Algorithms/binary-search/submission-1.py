class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            index = (l + r) // 2
            if nums[index] > target:
                r = index - 1
            elif nums[index] < target:
                l = index + 1
            else:
                return index

        return -1
        