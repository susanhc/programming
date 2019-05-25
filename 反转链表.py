'''
输入一个链表，反转链表后，输出新链表的表头。
解题思路：
  把头指针的下一个结点先赋给一个临时变量temp存储
  然后让pre指向当前结点的下一个结点
  再把当前结点的值赋给pre
  然后把存储的temp再赋给当前结点，这样就完成了一次转换
'''  
  
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        pre=None
        while pHead:
            temp=pHead.next
            pHead.next=pre
            pre=pHead
            pHead=temp
        return pre
