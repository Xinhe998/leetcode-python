# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.compareSym(root.left, root.right)

    def compareSym(self, left, right):
        """
        :type left: TreeNode
        :type right: TreeNode
        :rtype: bool
        """
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.compareSym(left.left, right.right) and self.compareSym(left.right, right.left)


s = Solution()
tree1 = TreeNode(2)
tree1.left = TreeNode(3)
tree1.left.left = TreeNode(4)
tree1.left.right = TreeNode(5)
tree1.left.right.left = TreeNode(8)
tree1.left.right.right = TreeNode(9)

tree1.right = TreeNode(3)
tree1.right.left = TreeNode(5)
tree1.right.right = TreeNode(4)
tree1.right.right.left = TreeNode(9)
tree1.right.right.right = TreeNode(8)

print s.isSymmetric(tree1)
