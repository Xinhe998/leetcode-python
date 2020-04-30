# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        l, r = 0, 0
        l += self.minDepth(root.left)
        r += self.minDepth(root.right)
        if l == 0:
            return r+1
        elif r == 0:
            return l+1
        else:
            return min(l, r) + 1


s = Solution()
# test case 1
tree1 = TreeNode(-10)
tree1.left = TreeNode(9)
tree1.right = TreeNode(20)
tree1.right.left = TreeNode(15)
tree1.right.right = TreeNode(7)
print(s.minDepth(tree1))

tree2 = TreeNode(5)
tree2.left = TreeNode(4)
tree2.left.left = TreeNode(11)
tree2.left.left.left = TreeNode(7)
tree2.left.left.right = TreeNode(2)
tree2.right = TreeNode(8)
tree2.right.left = TreeNode(13)
tree2.right.right = TreeNode(4)
tree2.right.right.right = TreeNode(1)
print(s.minDepth(tree2))

tree3 = TreeNode(1)
tree3.left = TreeNode(-2)
tree3.left.left = TreeNode(1)
tree3.left.left.left = TreeNode(-1)
tree3.left.right = TreeNode(3)
tree3.right = TreeNode(-3)
tree3.right.left = TreeNode(-2)
print(s.minDepth(tree3))
