from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        p = deque()
        level = 0
        x_parent = 0
        y_parent = 0
        x_level = 0
        y_level = 0
        prev = root
        p.append(root)
        while p:
            temp = p.popleft()
            if temp.val == x:
                x_parent = prev.val
            if temp.val == y:
                y_parent = prev.val
            if temp.left:
                p.append(temp.left)
                x_level += 1
            if temp.right:
                p.append(temp.right)
                y_level += 1
            prev = temp

        if x_level - y_level == 1 or y_level - x_level == 1and x_parent != y_parent:
            return True
        else:
            return False
