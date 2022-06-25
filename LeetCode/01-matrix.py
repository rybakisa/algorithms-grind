from collections import deque
from typing import List
import sys

class Solution_BFS:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        # specify allowed moves
        allowed_moves = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]
        visited = set()
        r_count = len(mat)
        c_count = len(mat[0])
        deq = deque()


        def dfs(target_value):
            while deq and mat[deq[0][0]][deq[0][1]] == target_value:
                r, c = deq.popleft()
                print(f'[+] visited {(r, c)}=={mat[r][c]}')
                visited.add((r, c))

                for move in allowed_moves:
                    nr, nc = r + move[0], c + move[1]
                
                    if (nr >= 0 and nr < r_count) \
                    and (nc >= 0 and nc < c_count) \
                    and (nr, nc) not in deq \
                    and (nr, nc) not in visited:
                        deq.append((nr, nc))
                        mat[nr][nc] = target_value + 1
            
            print(deq)
            print(visited)
            for r in mat:
                print(r)
            print()
            
        print('Zeroes')
        target_value = 0
        for r in range(r_count):
            for c in range(c_count):
                if mat[r][c] == target_value:
                    deq.append((r, c))

        while deq:
            print('Ones+')
            dfs(target_value)
            target_value += 1

        return mat


class Solution_BFS_2:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dist = [[sys.maxsize for _ in range(c_count)] for _ in range(r_count)]
        r_count, c_count = len(mat), len(mat[0])
        q = deque()

        for r in range(r_count):
            for c in range(c_count):
                if mat[r][c] == 0:
                    q.append((r, c))
                    dist[r][c] = 0
                    
        while q:
            print(q)
            r, c = q.popleft()
            distance = dist[r][c]

            neighbor_candidates = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            for n_row, n_col in neighbor_candidates:
                if 0 <= n_row < r_count \
                and 0 <= n_col < c_count \
                and dist[n_row][n_col] > distance + 1:
                    dist[n_row][n_col] = distance + 1
                    q.append((n_row, n_col))
        
        return dist


class Solution_DP:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        bottom_right = [(0, 1), (1, 0)]
        top_left = [(0, -1), (-1, 0)]
        r_count = len(mat)
        c_count = len(mat[0])
        visited = set()
        deq = deque()

        def update_value():
            pass

        def bfs(moves):
            while deq:
                r, c = deq.popleft()
                print(f'[+] visited {(r, c)}=={mat[r][c]}')
                visited.add((r, c))

                values = []
                for move in moves:
                    nr, nc = r - move[0], c - move[1]
                    print(nr, nc)
                    if (nr >= 0 and nr < r_count) \
                    and (nc >= 0 and nc < c_count) \
                    and mat[nr][nc] is not None:
                        values.append(mat[nr][nc])
                        print(f'[*][*] {mat[nr][nc]}')
                print(f'[+] {values}')

                if not values and mat[r][c] > 0 and moves[0][1] == 1:
                    mat[r][c] = None
                elif values and mat[r][c] is not None and mat[r][c] > 0:
                    if moves[0][1] == -1:
                        if mat[r][c] > min(values) + 1:
                            mat[r][c] = min(values) + 1
                            print(f'[+] changed {(r, c)}=={mat[r][c]}')
                    else:
                        if mat[r][c] < min(values) + 1:
                            mat[r][c] = min(values) + 1
                            print(f'[+] changed {(r, c)}=={mat[r][c]}')
                elif mat[r][c] is None:
                    mat[r][c] = min(values) + 1

                for move in moves:
                    nr, nc = r + move[0], c + move[1]
                    if (nr >= 0 and nr < r_count) \
                    and (nc >= 0 and nc < c_count) \
                    and (nr, nc) not in deq \
                    and (nr, nc) not in visited:
                        deq.append((nr, nc))


        for r in mat:
            print(r)
        print()
        deq.append((0, 0))
        bfs(bottom_right)

        for r in mat:
            print(r)
        print()
        visited = set()
        deq.append((r_count - 1, c_count - 1))
        bfs(top_left)

        for r in mat:
            print(r)
        print()

        return mat

mat = [
    [1,1,1,1,1],
    [1,0,1,1,1],
    [1,1,1,1,1],
    [1,1,1,0,1],
    [1,1,1,1,1],
]
print(Solution_BFS_2().updateMatrix(mat))
# print(Solution_DP().updateMatrix(mat))
