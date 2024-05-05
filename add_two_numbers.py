# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        add = 0  # 设定增加的值为0
        head = ListNode(0)  # 先设定一个头节点
        node = head  # 设置当前节点
        while l1 or l2:  # 循环结束条件为l1 且 l2 已经没有下一个节点了
            cur = ListNode(add)  # 生成一个节点
            if l1:
                cur.val += l1.val  # 当l1有节点的情况，增加值
                l1 = l1.next  # l1 取到下一个节点
            if l2:
                cur.val += l2.val
                l2 = l2.next
            add = cur.val // 10  # 取除完10的余数
            cur.val = cur.val % 10  # 取对10取的商值
            node.next, node = cur, cur  # 变换节点
        if add:
            node.next = ListNode(add)

        return head.next

l1 = [2, 4, 3]
l2 = [5, 6, 4]
Solution.addTwoNumbers(l1,l2)