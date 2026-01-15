from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## APPRAOCH 1: NAIVE APPROACH
class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def invertBinaryTree(self, root):
        if not root:
            return
        
        root.left, root.right = root.right, root.left
        self.invertBinaryTree(root.left)
        self.invertBinaryTree(root.right)
        return root

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        root.right = self.invertBinaryTree(root.right)
        return self.isSameTree(root.left, root.right)


## APPRAOCH 2: OPTIMAL APPROACH (WITHOUT CHANGING THE TREE)
class Solution2:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return (
            p.val == q.val and
            self.isMirror(p.left, q.right) and
            self.isMirror(p.right, q.left)
        )