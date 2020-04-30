# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.stack = []

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root or (not root.left and not root.right):
            return True
        self.check(root)
        for item in self.stack:
            if abs(item[0] - item[1]) > 1:
                return False
        return True

    def check(self, root):
      if not root:
            return 0
      if not root.left and not root.right:
          return 1
      l, r = 0, 0
      l += self.check(root.left)
      r += self.check(root.right)
      self.stack.append((l, r))
      if l == 0:
          return r+1
      elif r == 0:
          return l+1
      else:
          return max(l, r) + 1


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
tree2.right = TreeNode(2)
tree2.left.left = TreeNode(3)
tree2.left.right = TreeNode(3)
tree2.left.left.left = TreeNode(4)
tree2.left.left.right = TreeNode(4)

# test case 3
tree3 = TreeNode(1)
tree3.right = TreeNode(2)
tree3.right.right = TreeNode(3)


# test case 4
tree4 = TreeNode(1)
tree4.left = TreeNode(2)
tree4.left.left = TreeNode(3)
tree4.left.left.left = TreeNode(4)
tree4.right = TreeNode(2)
tree4.right.right = TreeNode(3)
tree4.right.right.right = TreeNode(4)

tree5 = TreeNode(1)

print(s.isBalanced(tree1))
# print(s.isBalanced(tree2))
# print(s.isBalanced(tree3))
# print(s.isBalanced(tree4))
# print(s.isBalanced(tree5))
