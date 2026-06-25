class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        def bfs(row, col):
            q = collections.deque()
            q.append((row, col))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            while q:
                row, col = q.popleft()
                for direction in directions:
                    tempR, tempC = direction
                    r, c = row + tempR, col + tempC
                    if r in range(rows) and c in range(cols) and grid[r][c] != -1 and grid[r][c] > grid[row][col] + 1:
                        grid[r][c] = grid[row][col] + 1
                        q.append((r, c))


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    bfs(i, j)

        