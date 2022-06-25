from hashlib import new
from typing import List

class Solution:
    # specify allowed moves
    allowed_moves = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]

    def paint(self, row, column, rows_count, columns_count, image, old_color, new_color):
        print(image)
        print(f'[+] painting {(row, column)}')
        image[row][column] = new_color

        for move in Solution.allowed_moves:
            new_row = row + move[0]
            new_column = column + move[1]
            print(f'[+] trying {(new_row, new_column)}')

            if (new_row >= 0 and new_row < rows_count) \
            and (new_column >= 0 and new_column < columns_count) \
            and image[new_row][new_column] == old_color:
                self.paint(new_row, new_column, rows_count, columns_count, image, old_color, new_color)


    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # get color from source cell
        old_color = image[sr][sc]
        print(old_color)
        if old_color == newColor:
            return image    

        r_count = len(image)
        c_count = len(image[0])

        self.paint(sr, sc, r_count, c_count, image, old_color, newColor)
            
        return image



image = [[0,0,0],[1,0,0]]
sr = 1
sc = 0
newColor = 2

print(image)
print(
    Solution().floodFill(image, sr, sc, newColor)
)
