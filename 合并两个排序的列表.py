'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
解题思路：使用归并法，注意把合并后的链表的类先赋给另一个类，这样每次循环后输出一个值，否则输出的只是新添加的值
'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        dummy = ListNode(0)
        pHead = dummy

        while pHead1 and pHead2:
            if pHead1.val >= pHead2.val:
                dummy.next = pHead2
                pHead2 = pHead2.next
            else:
                dummy.next = pHead1
                pHead1 = pHead1.next

            dummy=dummy.next
        if pHead1:
            dummy.next = pHead1
        elif pHead2:
            dummy.next = pHead2
        return pHead.next
