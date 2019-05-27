'''
二叉树的子树和子结构：
子树的意思是只要包含了一个结点，就得包含这个结点下的所有结点
子结构的意思是包含了一个结点，可以只取左子树或右子树，或者都不取
树有5种结构，包括只含右子树不含左子树的情况，所以这种也算一种子结构

解题思路：
先比较树的根节点，如果相等，递归比较左右子树
如果不相等，递归比较左右子树和proot2是否相等
一共有两个递归。
'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, proot1, proot2):
        result=False
        if proot1!=None and proot2!=None:
            if proot1.val==proot2.val:
                result=self.same(proot1,proot2)
            if not result:
                result=self.HasSubtree(proot1.left,proot2)
            if not result:
                result=self.HasSubtree(proot1.right,proot2)
        return result
    def same(self,proot1,proot2):
        if proot2==None:
            return True
        if proot1==None:
            return False
        if proot1.val!=proot2.val:
            return False
        return self.same(proot1.left,proot2.left) and self.same(proot1.right,proot2.right)
