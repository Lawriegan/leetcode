# Definition for singly-linked list.
import copy
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pre = ListNode(0.)
        pre.next = head
        pre_del = cur = pre

        for i in range(n + 1):
            cur = cur.next
        while cur:
            pre_del = pre_del.next
            cur = cur.next

        pre_del.next = pre_del.next.next
        return pre.next

