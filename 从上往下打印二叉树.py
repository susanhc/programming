'''
题目描述
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''
'''
解题思路
创建一个队列，每次弹出根结点，然后添加它的左右结点到队列中
'''
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if not root:
            return []
        queue=[]
        result=[]
        queue.append(root)
        while(len(queue)>0):
            node=queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result
