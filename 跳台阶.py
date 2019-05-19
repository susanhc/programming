# -*- coding: utf-8 -*-
"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
"""
class Solution:
    def jumpFloor(self, number):
        res=[1,2]
        while len(res)<=number:
            res.append(res[-1]+res[-2])
        if number==1:
            return 1
        else:
            return res[number-1]
