from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'[{self.val} {self.next}]'

def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = head
    fast = head

    while fast and fast.next:
        print('***', slow, fast)
        slow = slow.next
        fast = fast.next.next

    return slow


head = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))))
print(middleNode(head))
