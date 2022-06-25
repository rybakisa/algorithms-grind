from typing import List
from collections import deque


class Solution:
    def __init__(self) -> None:
        self.allowed_moves = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

        self.cur_area = 0
        self.max_area = 0

        self.grid = []
        self.r_count = 0
        self.c_count = 0

        self.deq = deque()
        self.ones = deque()


    def updateMax(self):
        self.max_area = self.cur_area if self.cur_area > self.max_area else self.max_area
        self.cur_area = 0

    def processONes(self):
        print('[*][*] Processing ones!')
        while self.ones:
            print('[*][*] Ones:', self.ones)
            cr, cc = self.ones.popleft()
            print(f'[*][-] Pop from ones {(cr,cc)} == {self.grid[cr][cc]}')
            self.grid[cr][cc] = None
            print(f'[*][*] {(cr,cc)} == {self.grid[cr][cc]}')
            self.cur_area += 1
            print(f'[*][*] Areas: {self.cur_area}/{self.max_area}')
            self.checkNeighbors(cr, cc, 1)
        self.updateMax()

    def checkNeighbors(self, r, c, mode=0):
        for move in self.allowed_moves:
            nr = r + move[0]
            nc = c + move[1]

            if (nr >= 0 and nr < self.r_count) \
            and (nc >= 0 and nc < self.c_count) \
            and not (nr, nc) in self.deq \
            and not (nr, nc) in self.ones \
            and not self.grid[nr][nc] == None:
                print(f'[*] Checking {(nr,nc)} == {self.grid[nr][nc]}')
                if self.grid[nr][nc] == 0:
                    self.deq.append((nr, nc))
                    print(f'[+] Enqueue to dec {(nr,nc)} == {self.grid[nr][nc]}')
                elif self.grid[nr][nc] == 1:
                    self.ones.appendleft((nr, nc))
                    if mode == 0:
                        self.processONes()



    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.r_count = len(self.grid)
        self.c_count = len(self.grid[0])

        self.deq.append((0, 0))
        while self.deq:
            print()
            print(f'Processing {self.deq}')
            for r in self.grid:
                print(r)

            r, c = self.deq.popleft()
            value = self.grid[r][c]
            print(f'[-] Dequeue from deq {(r,c)} == {self.grid[r][c]}')
            
            if value == 1:
                self.ones.appendleft((r, c))
                print(f'[+] Push to ones {(r,c)} == {self.grid[r][c]}')
                self.processONes()
                
            elif value == None:
                print('[WARN] double visit')
                pass
            
            self.grid[r][c] = None
            self.checkNeighbors(r, c)

        self.updateMax()
        return self.max_area
            

class Solution_2:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r_count = len(grid)
        c_count = len(grid[0])
        
        def dfs(r, c):

            if grid[r][c] == 1:    
                #eraze it to avoid repitition
                grid[r][c] = 0
                
                count = 1

                if r > 0 and grid[r-1][c] == 1:
                    count += dfs(r-1, c)
                if r+1 < r_count and grid[r+1][c] == 1:
                    count += dfs(r+1,c)
                if c > 0 and grid[r][c-1] == 1:
                    count += dfs(r, c-1)
                if c+1 < c_count and grid[r][c+1] == 1:
                    count += dfs(r, c+1)

                return count
            return 0
        
        area = 0
        for r in range(r_count):
            for c in range(c_count):
                if grid[r][c] == 1:
                    area = max(area, dfs(r,c))
        return area


grid1 = [
    [0,1,1,0],
    [0,0,1,0],
    [1,1,0,1],
]
grid2 = [[0,1],[1,0]]
grid3 = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
grid4 = [[0,0,0,0,0,0]]
grid5 = [
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,0,1,1],
    [0,0,0,1,1],
]
# print(Solution().maxAreaOfIsland(grid))

print(Solution_2().maxAreaOfIsland(grid1))
print(Solution_2().maxAreaOfIsland(grid2))
print(Solution_2().maxAreaOfIsland(grid3))
print(Solution_2().maxAreaOfIsland(grid4))
print(Solution_2().maxAreaOfIsland(grid5))
