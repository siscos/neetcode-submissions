# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _dfs(self, node: Optional[TreeNode]) -> tuple[bool, int]:
        if node is None:
            return True, 0

        left, right = self._dfs(node.left), self._dfs(node.right)

        if not left[0] or not right[0] or abs(left[1] - right[1]) > 1:
            return False, -1

        return True, 1 + max(left[1], right[1])

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self._dfs(root)[0]
