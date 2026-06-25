class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        for token in tokens:
            if token == '+':
                val1 = stack.pop()
                val2 = stack.pop()
                result = int(val1) + int(val2)
                stack.append(result)
                continue
            elif token == '-':
                val1 = stack.pop()
                val2 = stack.pop()
                result = int(val2) - int(val1)
                stack.append(result)
                continue
            elif token == '*':
                val1 = stack.pop()
                val2 = stack.pop()
                result = int(val1) * int(val2)
                stack.append(result)
                continue
            elif token == '/':
                val1 = stack.pop()
                val2 = stack.pop()
                result = int(int(val2) / int(val1))
                stack.append(result)
                continue
            stack.append(token)

        return int(stack[-1])