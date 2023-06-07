# Binary Tree Node Sum

This is a Python solution to check if the value of the root node in a binary tree is equal to the sum of its left and right child nodes.

# Problem Description

Given a binary tree with the following structure:
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

Implement the checkTree method in the Solution class, which takes a root node of type TreeNode as input and returns a boolean value. The method should return True if the value of the root node is equal to the sum of the values of its left and right child nodes. Otherwise, it should return False.