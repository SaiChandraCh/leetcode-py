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
            while p and q:
                temp1 = p.popleft()
                temp2 = q.popleft()
                temp1.val += temp2.val
                if temp1.left and temp2.left:
                    p.append(temp1.left)
                    q.append(temp2.left)
                if temp1.left and not temp2.left:
                    pass
                if not temp1.left and temp2.left:
                    temp1.left = temp2.left
                    # q.append(TreeNode(0))
                if temp1.right and temp2.right:
                    p.append(temp1.right)
                    q.append(temp2.right)
                if temp1.right and not temp2.right:
                    pass
                if not temp1.right and temp2.right:
                    temp1.right = temp2.right

            # while q:
            #     temp2 = q.popleft()
            #     if temp2.left:
            #         q.append(temp2.left)
            #     if temp2.right:
            #         q.append(temp2.right)
        return t1

if __name__ == "__main__":
    obj = Solution()
    t1 = TreeNode(1)
    t1.left = TreeNode(5)
    t1.right = TreeNode(6)
    # t1.left.left = TreeNode(5)
    t2 = TreeNode(2)
    # t2.left = TreeNode(1)
    t2.right = TreeNode(4)
    # t2.left.right = TreeNode(4)
    t2.right.right = TreeNode(7)
    obj.mergeTrees(t1,t2)