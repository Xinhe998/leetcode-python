# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __iter__(self):
        node = self
        while node:
            yield node
            node = node.next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tmp = ListNode(None)
        tmp_current_node = tmp

        while l1 or l2:
            if l2 is None:
                tmp_current_node.next = ListNode(l1.val)
                l1 = l1.next
                tmp_current_node = tmp_current_node.next

            elif l1 is None:
                tmp_current_node.next = ListNode(l2.val)
                l2 = l2.next
                tmp_current_node = tmp_current_node.next

            else:
                if l1.val <= l2.val:
                    tmp_current_node.next = ListNode(l1.val)
                    l1 = l1.next
                    tmp_current_node = tmp_current_node.next
                else:
                    tmp_current_node.next = ListNode(l2.val)
                    l2 = l2.next
                    tmp_current_node = tmp_current_node.next

        return tmp.next


s = Solution()
l1 = ListNode(3)
l1.next = ListNode(4)
l1.next.next = ListNode(4)
l2 = ListNode(2)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
s.mergeTwoLists(l1, l2)
