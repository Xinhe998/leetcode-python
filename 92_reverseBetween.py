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
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n or not head.next:
            return head

        stack = []
        current = head
        point1, point2, prev = None, None, None

        i = 1
        while i <= n:
            if i >= m and i <= n:
                if i == m:
                    point1 = prev
                elif i == n:
                    point2 = current.next
                stack.append(current)
            i += 1
            prev, current = current, current.next

        while stack:
            node = stack.pop()
            if point1:
                point1.next = node
            else:
                head = node
            point1 = node
        point1.next = point2
        return head


s = Solution()
l1 = ListNode(1)
current = l1.next
for i in [2, 3, 4, 5]:
    current = ListNode(i)
    current = current.next
s.reverseBetween(l1, 2, 4)
