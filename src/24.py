# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            prev = head
            curr = prev.next
            if not curr:
                return head
            else:
                head = curr
                flag = False
                while prev.next:
                    curr = prev.next
                    if curr.next:
                        prev.next = curr.next
                    else:
                        curr.next = prev
                        break
                    if flag:
                        if prev.next:
                            prev = prev.next
                            curr.next = prev.next
                            prev.next = curr
                            prev = curr
                    else:
                        flag = True
                        curr.next = prev
        return head


if __name__ == "__main__":
    obj = Solution()
    head = ListNode(1)
    temp = head
    temp.next = ListNode(2)
    # temp = temp.next
    # temp.next = ListNode(3)
    # temp = temp.next
    # temp.next = ListNode(4)
    # temp = temp.next
    # temp.next = ListNode(5)
    print obj.swapPairs(head)
