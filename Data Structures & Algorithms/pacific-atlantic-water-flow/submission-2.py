class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        # keep a list of visited sets for pacific and atlantic
        pacific, atlantic = set(), set()

        # r: row index
        # c: column index
        # visited: set of visited node in the grid
        # prevHeight: previous water height 
        def dfs(r, c, visited, prevHeight):
            # base case
            if r not in range(rows) or c not in range(cols) or (r, c) in visited or heights[r][c] < prevHeight:
                return

            visited.add((r, c))
            # recursive traverse through all directions
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            

        # go through the top and bottom rows 
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c]) 
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])

        # go through left most and right most column
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        # loop through every index and check if they are visited
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])
        return result