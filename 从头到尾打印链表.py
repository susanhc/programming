# -*- coding: utf-8 -*-
"""
题目：输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
解题思路：输入的链表的尾是得到数组的头，所以可以使用头插法
l.inset（index，val）是先是插入的位置，然后是插入的值
注意链表的声明，包含值和指针
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if not listNode:
            return []
        else:
            head=listNode
            l=[]
            while head:
                l.insert(0,head.val)
                head=head.next
            return l