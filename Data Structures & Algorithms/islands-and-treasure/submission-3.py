class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # multi-source BFS
        # append all 0 into the queue first
        q = collections.deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j))

        # bfs into the queue
        while q:
            qR, qC = q.popleft()
            for dR, dC in direction:
                r, c = qR + dR, qC + dC
                
                if r in range(rows) and c in range(cols) and grid[r][c] == 2147483647:
                    grid[r][c] = grid[qR][qC] + 1
                    q.append((r, c))

        