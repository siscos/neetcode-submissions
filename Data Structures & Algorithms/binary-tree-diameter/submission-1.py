# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    _diameter: int = 0

    def _dfs(self, root: Optional[TreeNode]) -> int:
            if root is None:
                return 0

            left_depth = self._dfs(root.left)
            right_depth = self._dfs(root.right)

            self._diameter = max(self._diameter, left_depth + right_depth)

            return 1 + max(left_depth, right_depth)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self._dfs(root)

        return self._diameter