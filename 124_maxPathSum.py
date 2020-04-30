# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.max_val = 0

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_val = root.val
        self.dfs(root)
        return self.max_val

    def dfs(self, root):
        left = self.dfs(root.left) if root.left else 0
        right = self.dfs(root.right) if root.right else 0
        middle = max(root.val, root.val+right, root.val+left)
        self.max_val = max(self.max_val, middle, root.val+right+left)
        return middle


s = Solution()
# test case 1
tree1 = TreeNode(-10)
tree1.left = TreeNode(9)
tree1.right = TreeNode(20)
tree1.right.left = TreeNode(15)
tree1.right.right = TreeNode(7)

# test case 2
tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(3)

# test case 3
tree3 = TreeNode(-3)

# test case 4
tree4 = TreeNode(-2)
tree4.left = TreeNode(-1)

# test case 5
tree5 = TreeNode(1)
tree5.left = TreeNode(2)

# test case 6
tree6 = TreeNode(-2)
tree6.right = TreeNode(-3)

# test case 7
tree7 = TreeNode(1)
tree7.left = TreeNode(-2)
tree7.right = TreeNode(3)

# test case 8
tree8 = TreeNode(1)
tree8.left = TreeNode(-2)
tree8.left.left = TreeNode(1)
tree8.left.left.left = TreeNode(-1)
tree8.left.right = TreeNode(3)
tree8.right = TreeNode(-3)
tree8.right.left = TreeNode(-2)

# test case 9
tree9 = TreeNode(5)
tree9.left = TreeNode(4)
tree9.left.left = TreeNode(11)
tree9.left.left.left = TreeNode(7)
tree9.left.left.right = TreeNode(2)
tree9.right = TreeNode(8)
tree9.right.left = TreeNode(13)
tree9.right.right = TreeNode(4)
tree9.right.right.right = TreeNode(1)

print('expected= 42', s.maxPathSum(tree1))
print('expected= 6', s.maxPathSum(tree2))
print('expected= -3', s.maxPathSum(tree3))
print('expected= -1', s.maxPathSum(tree4))
print('expected= 3', s.maxPathSum(tree5))
print('expected= -2', s.maxPathSum(tree6))
print('expected= 4', s.maxPathSum(tree7))
print('expected= 3', s.maxPathSum(tree8))
print('expected= 48', s.maxPathSum(tree9))
