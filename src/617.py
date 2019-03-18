from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and t2:
            return t2
        if t1 and not t2:
            return t1
        if t1 and t2:
            p = deque()
            q = deque()
            p.append(t1)
            q.append(t2)
            temp3 = None
            left = True
            right = False
            while p or q:
                temp1 = p.pop()
                temp2 = q.pop()
                if temp1 and temp2:
                    if not temp3:
                        temp3 = TreeNode(temp1.val + temp2.val)
                    else:
                        if left:

                            right = True
                            left = False
                        if right:
                            right = False
                            left = True
                elif temp2 and not temp1:
                    print
                if temp1:
                    p.append(temp1.left)
                    p.append(temp2.left)
                if temp2:
                    q.append(temp1.left)
                    q.append(temp2.left)


if __name__ == "__main__":
    obj = Solution()
    t1 = TreeNode(1)
    t1.left = TreeNode(3)
    t1.right = TreeNode(2)
    t1.left.left = TreeNode(5)
    t2 = TreeNode(2)
    t2.left = TreeNode(1)
    t2.rigth = TreeNode(3)
    t2.left.right = TreeNode(4)
    t2.rigth.right = TreeNode(7)
    obj.mergeTrees(t1,t2)