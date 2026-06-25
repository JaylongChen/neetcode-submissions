class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        # convert to (position, speed)
        for i in range(len(position)):
            pos, s = position[i], speed[i]
            pairs.append([pos, s])

        pairs.sort(reverse = True)
        stack = []
        
        # calculate the speed stack
        for pair in pairs:
            stack.append((target - pair[0]) / pair[1]) #calculate speed
            if len(stack) > 1 and stack[-1] <= stack[-2]: #if last car catch up to the one before
                stack.pop()

        return(len(stack))