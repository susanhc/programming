# -*- coding: utf-8 -*-
"""

用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
栈A和B用两个列表来表示，列表的有pop弹出函数
先在栈A中添加元素，完成push操作，然后把A中的元素弹出到B中，这时A和B中的元素就是相反的了
B再弹出这样就完成了先进先出即队列的pop操作

"""
class Solution:
    def __init__(self):
        self.stackA=[]
        self.stackB=[]
    def push(self, node):
        return self.stackA.append(node)
    def pop(self):
        if self.stackB:
            return self.stackB.pop()
        elif not self.stackA:
            return None
        else:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()