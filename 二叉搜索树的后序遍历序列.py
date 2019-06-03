'''
题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
'''
'''
解题思路

二叉搜索树（二叉查找树，二叉排序树）它或者是一棵空树，或者是具有下列性质的二叉树： 若它的左子树不空，
则左子树上所有结点的值均小于它的根结点的值； 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 它的左、右子树也分别为二叉排序树。

用递归的思想。

把数组分成三部分，比如[4,8,6,12,16,14,10]，10就是根节点，4,8,6都是左子树，12,16,14,10都是右子树，
然后针对左右子树再去判断是不是符合根节点、左右子树这一个规律（左子树都比根节点小，右子树都比根节点大）
'''
class Solution:
    def VerifySquenceOfBST(self, se):
        if not se:
            return False
        for i in range(len(se)):
            if se[i]>se[-1]:
                break
        index=i
        for j in range(i,len(se)):
            if se[j]<se[-1]:
                return False
        left=True
        right=True
        if len(se[:index])>0:
            left=self.VerifySquenceOfBST(se[:index])
        if len(se[index:-1])>0:
            right=self.VerifySquenceOfBST(se[index:-1])
        return left and right
