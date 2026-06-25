class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def bfs(row, col):
            nonlocal maxArea
            area = 1
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            q = collections.deque()
            q.append((row, col))

            while q:
                tempR, tempC = q.popleft()
                for direction in directions:
                    dr, dc = direction
                    r, c = tempR + dr, tempC + dc

                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))
                        area += 1
            maxArea = max(maxArea, area)


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    visited.add((i, j))
                    bfs(i, j)

        return maxArea