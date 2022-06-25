from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r_count, c_count = len(grid), len(grid[0])
        q = deque()

        # fing all rotten oranges O(m*n)
        for r in range(r_count):
            for c in range(c_count):
                if grid[r][c] == 2:
                    q.append((r, c))
                    grid[r][c] = 3
        
        # bfs through fresh and count iterations
        minutes = self.bfs(grid, r_count, c_count, q)
        
        # check if there are fresh oranges left
        for r in range(r_count):
            for c in range(c_count):
                if grid[r][c] == 1:
                    return -1
                
        return minutes

    def bfs(self, grid, r_count, c_count, q):
        minutes = -1 if q else 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                self.check_neighbors(grid, r_count, c_count, q, r, c)    
            minutes += 1
        
        return minutes

    def check_neighbors(self, grid, r_count, c_count, q, r, c):
        allowed_moves = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

        for dr, dc in allowed_moves:
            nr, nc = r + dr, c + dc

            if 0 <= nr < r_count \
            and 0 <= nc < c_count \
            and (nr, nc) not in q \
            and grid[nr][nc] == 1:
                grid[nr][nc] = 3
                q.append((nr, nc))


# grid = [
#     [2,2,2],
#     [2,2,2],
#     [2,2,2]
# ]
grid = [[0]]
print(Solution().orangesRotting(grid))
