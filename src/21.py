class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution(object):
def mergeTwoLists():
    l1 = ListNode(5)
    temp1 = l1
    temp1.next = ListNode(10)
    temp1 = temp1.next
    temp1.next = ListNode(15)
    temp1 = temp1.next
    temp1.next = ListNode(22)
    temp1 = temp1.next
    temp1.next = ListNode(28)
    l2 = ListNode(1)
    temp2 = l2
    temp2.next = ListNode(8)
    temp2 = temp2.next
    temp2.next = ListNode(13)
    temp2 = temp2.next
    temp2.next = ListNode(19)
    temp2 = temp2.next
    temp2.next = ListNode(21)
    temp = None
    res = None
    if (l1 == None):
        return l2
    if (l2 == None):
        return l1

    while (l1 != None and l2 != None):
        if (l1.val > l2.val):
            if (res == None):
                res = l2
                temp = res
            else:
                temp.next = l2
                temp = temp.next
            l2 = l2.next
        else:
            if (res == None):
                res = l1
                temp = res
            else:
                temp.next = l1
                temp = temp.next
            l1 = l1.next

    if (l2 != None):
        temp.next = l2
    if (l1 != None):
        temp.next = l1

    return res


mergeTwoLists()