class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        visited = set()
        result = 0
        rows = len(grid)
        cols = len(grid[0])

        def bfs(row, col):
            q = collections.deque()
            q.append((row, col))
            visited.add((row, col))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while q:
                tempr, tempc = q.popleft()
                # check each direction that if the island can be extended
                for direction in directions:
                    directionR, directionC = direction
                    r, c = tempr + directionR, tempc + directionC

                    if r in range(rows) and c in range(cols) and grid[r][c] == '1' and (r, c) not in visited:
                        visited.add((r, c))
                        q.append((r, c))
            
        # traverse through the grid
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    bfs(i, j)
                    result += 1

        return result
                