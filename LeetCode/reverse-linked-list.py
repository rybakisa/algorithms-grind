from hashlib import new
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self) -> str:
        return f'{self.val} => {self.next}'

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        last_node = new_node = ListNode(head.val)

        while head.next:
            head = head.next

            new_node = ListNode()
            new_node.val = head.val
            new_node.next = last_node

            last_node = new_node
        
        return new_node

head = ListNode(1, ListNode(2, ListNode(4, None)))
print(Solution().reverseList(head))
