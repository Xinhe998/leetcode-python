# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.heapify(p) == self.heapify(q)

    def heapify(self, tree):
        if not tree:
            return [None]
        if not tree.left and not tree.right:
            return [tree.val]
        return [tree.val] + self.heapify(tree.left) + self.heapify(tree.right)


s = Solution()
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)
tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(2)
print s.isSameTree(tree1, tree2)
