# -*- coding: utf-8 -*-
"""
输入一个链表，输出该链表中倒数第k个结点

利用列表切片 
"""

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if not head:
            return None
        l=[]
        while(head):
            l.append(head)
            head=head.next
        if k>len(l) or k<1:
            return None
        return l[-k]
