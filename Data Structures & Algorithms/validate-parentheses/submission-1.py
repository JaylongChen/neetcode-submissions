class Solution:
    def isValid(self, s: str) -> bool:
        pair = {')' : '(',
                ']' : '[',
                '}' : '{'}
        stack = []
        
        for char in s:
            if char in pair.values():
                stack.append(char)
            elif char in pair.keys():
                if len(stack) == 0:
                    return False
                elif pair[char] != stack.pop():
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
            