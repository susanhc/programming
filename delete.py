# -*- coding: utf-8 -*-
"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定数组 nums = [1,1,2],
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
你不需要考虑数组中超出新长度后面的元素。

解题思路
第一反应是把列表转换成集合，利用集合的不可重复性来删除重复的元素，但这样做的结果并不能改变原来的列表中的元素，而是产生了一个新的列表。
过程中还想到了深拷贝，复习一下
import copy
l=[1,2,3]
l1=copy.deepcopy(l)
最后利用列表元素进行比较的方法删除，但只能从后边删除，即从后往前比较，注意要单独考虑列表元素为空的情况

"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        else:
            i=len(nums)-1
            while i!=0:
                if nums[i]==nums[i-1]:
                    del nums[i]
                i-=1
            return len(nums)

