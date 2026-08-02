# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _get_height(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        
        return 1 + max(self._get_height(node.left), self._get_height(node.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        if abs(self._get_height(root.left) - self._get_height(root.right)) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
        