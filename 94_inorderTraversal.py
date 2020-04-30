# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
          return []
        result = []
        if root.left:
          result += self.inorderTraversal(root.left)
        result.append(root.val)
        if root.right:
          result += self.inorderTraversal(root.right)
        return result

s = Solution()
tree1 = TreeNode(1)
tree1.right = TreeNode(2)
tree1.right.left = TreeNode(3)

print(s.inorderTraversal(tree1))