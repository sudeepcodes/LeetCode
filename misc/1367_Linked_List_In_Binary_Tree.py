# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def check_exists(ll, tree):
            if not ll:
                return True
            if not tree:
                return False
            if ll.val != tree.val:
                return False
            return check_exists(ll.next, tree.left) or check_exists(ll.next, tree.right)
        
        def dfs(node):
            if not node:
                return False
            if check_exists(head, node):
                return True
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)

            
