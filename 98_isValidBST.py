# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.last = None

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if not self.isValidBST(root.left):
            return False
        if self.last and root.val <= self.last.val:
            return False
        self.last = root
        return self.isValidBST(root.right)


s = Solution()
# test case 1
tree1 = TreeNode(10)
tree1.left = TreeNode(5)
tree1.right = TreeNode(15)
tree1.right.left = TreeNode(6)
tree1.right.right = TreeNode(20)

# test case 2
# tree1 = TreeNode(2)
# tree1.right = TreeNode(3)
# tree1.left = TreeNode(1)

# test case 3
# tree1 = TreeNode(0)

# test case 4
# tree1 = TreeNode(3)
# tree1.right = TreeNode(30)


print s.isValidBST(tree1)
