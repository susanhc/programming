'''
题目：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字
均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4，5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就
不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
'''
'''
解题思路：
①一共需要三个栈：入栈序列pushv、出栈序列popv、缓冲栈stack
②先比较pushv和popv第一个元素是否相等（a.pop(0)表示弹出列表的第一个元素，a.pop()表示弹出最后一个元素）
  如果相等，分别从两个序列中弹出元素1
③不相等的话，比较缓冲序列stack的最后一个元素和popv的第一个元素，相等的话把它们分别弹出
④不相等的话，看pushv是否还有元素，有就继续往stack中添加，直到添加到和popv的首个元素相等为止
⑤这时候如果stack[-1]和popv[0]不相等，pushv中又没有元素了，就说明二者的顺序是不一样的，返回False
⑥最后如果popv为空，则返回True

class Solution:
    def IsPopOrder(self, pushV, popV):
        stack=[]
        while popV:
            if pushV and pushV[0]==popV[0]:
                pushV.pop(0)
                popV.pop(0)
            elif stack and stack[-1]==popV[0]:
                stack.pop()
                popV.pop(0)
            elif pushV:
                stack.append(pushV.pop(0))
            else:
                return False
        return True
