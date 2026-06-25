class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        # only complete when n = #openBracket = #closedBracket
        # always add ( when #openBracket < n
        # if #openBracket > #closedBracket, add a (
        # if #openBracket < #closedBracket, add a )

        def backtrack(numOpen, numClose):
            if numOpen == numClose == n:
                temp = ''
                for bracket in stack:
                    temp += bracket
                result.append(temp)
                
                return

            if numOpen <= n:
                stack.append('(')
                backtrack(numOpen + 1, numClose)
                stack.pop()

            if numOpen > numClose:
                stack.append(')')
                backtrack(numOpen, numClose + 1)
                stack.pop()

            

        backtrack(0, 0)

        return result