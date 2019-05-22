# -*- coding: utf-8 -*-
"""
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示
由于是二进制，如果有一位是1的话，那么比他小1的数，和他相与，会得到从这位开始全0的数，前边的不变，
直到数n全变为0为止
因为负数是用补码表示，和0xffffffff相与可以得到其补码，即取反加一，然后再利用上述方法算1的个数
"""
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        if n==0:
            return 0
        if n<0:
            n=n&0xffffffff
        cnt=0
        while n:
            cnt+=1
            n=n&(n-1)
        return cnt
