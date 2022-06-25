from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'[{self.val} {self.next}]'


class Solution:
    def get_element_and_his_prev(self, search_from, steps):
        prev_element = None
        element = search_from
        for i in range(steps):
            prev_element = element
            element = element.next
        
        return prev_element, element


    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        mid = fast = head
        mid_i = end_i = 0
        
        while fast and fast.next:
            mid = mid.next
            mid_i += 1
            fast = fast.next.next
            end_i += 2

        if fast and not fast.next:
            end_i += 1

        target_i = end_i - n
        print(end_i, mid_i, n, target_i)

        if target_i > mid_i:
            # print(1)
            prev, target = self.get_element_and_his_prev(mid, target_i - mid_i)
        elif target_i <= mid_i:
            # print(2)
            prev, target = self.get_element_and_his_prev(head, target_i)

        print(prev, target)
        if prev:
            prev.next = target.next
        else:
            head = target.next

        return head


head = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None)))))))
print(Solution().removeNthFromEnd(head, 7))

