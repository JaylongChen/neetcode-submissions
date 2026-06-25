class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1

        while l <= r:
            speed = (l + r) // 2
            count = 0
            for pile in piles:
                count += math.ceil(pile / speed)
            if count > h:                
                l = speed + 1
            elif count <= h:
                r = speed - 1
        return l
            
            
