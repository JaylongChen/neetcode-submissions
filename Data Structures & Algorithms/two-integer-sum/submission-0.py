class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dih = {}
        for index, num in enumerate(nums):
            temp = target - num
            if temp in dih:
                return [dih[temp], index]
            else:
                dih[num] = index