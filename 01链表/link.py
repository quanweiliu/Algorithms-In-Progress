# Definition for singly-linked list.
from traceback import print_tb


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


p = ListNode()
print(p.next==None)
