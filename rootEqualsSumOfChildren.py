class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if root.val == (root.right.val + root.left.val):
            return True
        return False


# Test Case
root = TreeNode(10)
root.left = TreeNode(4)
root.right = TreeNode(6)

solution = Solution()
print(solution.checkTree(root))

# Expected output: True, as the value of the root (10) is equal to the sum of the values of its left and right child nodes
