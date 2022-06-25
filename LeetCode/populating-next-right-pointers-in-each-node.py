from collections import deque
from turtle import right
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __str__(self) -> str:
        return f'[{self.val} => {self.next}]'


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        level = 0
        level_elems_count = 0

        q = deque()
        q.append(root)
        while q:
            node = q.popleft()

            level_elems_count += 1
            if level_elems_count == 2**level:
                level += 1
                level_elems_count = 0
            else:
                if q:
                    node.next = q[0]

            if node.left:
                q.append(node.left)
                q.append(node.right)

        return root


class Solution_2:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root or not root.left:
            return root
        
        root.left.next = root.right
        root.right.next = root.next.left if root.next else None

        self.connect(root.left)
        self.connect(root.right)

        return root



# root = Node(
#     1,
#     Node(
#         2,
#         Node(4),
#         Node(5),
#         None,
#     ),
#     Node(
#         3,
#         Node(6),
#         Node(7),
#         None,
#     ),
#     None,
# )
root = Node()
print(Solution().connect(None))
