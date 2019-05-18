# -*- coding: utf-8 -*-
"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39

实现这个主要可以采用递归的方法，所以一开始写出代码一，但耗时太长未通过
方法二巧妙的利用列表，通过索引尾部的两个数相加后即得下一个数
判断n的长度和列表的长度是否一致，不一致就需要添加

"""
#方法一
class Solution:
    def Fibonacci(self, n):
        while n<=39:
            if n==0:
                return 0
            elif n==1:
                return 1
            else:
                return self.Fibonacci(n-1)+self.Fibonacci(n-2)

#方法二
class Solution:
    def Fibonacci(self, n):
        res=[0,1]
        while len(res)<=n:
            res.append(res[-1]+res[-2])
        return res[n]