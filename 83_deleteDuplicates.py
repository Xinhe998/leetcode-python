class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        i, j = head, head.next
        while j != None:
            if i.val != j.val:
                i.next = j
                i, j = j, j.next
            else:
                j = j.next
        i.next = None


s = Solution()
l1 = ListNode(None)
current = l1.next
for i in [2, 3, 3, 3]:
    current = ListNode(i)
    current = current.next
s.deleteDuplicates(l1)
