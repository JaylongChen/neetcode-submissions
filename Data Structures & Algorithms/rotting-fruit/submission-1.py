class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        result = 0
        rows = len(grid)
        cols = len(grid[0])
        q = collections.deque()
        fresh = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # add all rotten bananas to queue
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        while q and fresh > 0:
            for _ in range(len(q)):
                qr, qc = q.popleft()
                for dr, dc in directions:
                    r, c = qr + dr, qc + dc

                    if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                        grid[r][c] = 2
                        q.append((r, c))
                        fresh -= 1

            result += 1

        if fresh > 0:
            return -1
        else:
            return result