from hashlib import new
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self) -> str:
        return f'{self.val} => {self.next}'

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur_node = ListNode()

        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            cur_node.val = list1.val
            cur_node.next = self.mergeTwoLists(list1.next, list2)
        else:
            cur_node.val = list2.val
            cur_node.next = self.mergeTwoLists(list1, list2.next)

        return cur_node
        

list1 = ListNode(1, ListNode(2, ListNode(4, None)))
list2 = ListNode(1, ListNode(3, ListNode(4, None)))
print('Answer', Solution().mergeTwoLists(list1, list2))