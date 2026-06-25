class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        result = []

        for index in range(n):
            product = 1
            for i in range(n):
                if i == index:
                    continue
                product *= nums[i]
            result.append(product)
            

        return result