class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        length = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                temp = num
                temp_length = 1           
                while temp + 1 in nums_set:
                    temp_length += 1
                    temp += 1
                if temp_length > length:
                    length = temp_length
        return length