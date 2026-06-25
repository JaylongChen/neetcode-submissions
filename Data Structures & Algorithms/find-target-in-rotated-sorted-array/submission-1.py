class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            # check if left half is sorted
            elif nums[l] <= nums[m]:
                if nums[l] <= target and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            
            else:
                if target <= nums[r] and nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
        return -1