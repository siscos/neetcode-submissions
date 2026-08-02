# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _get(self, root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        if root is None:
            return None

        if min(p.val, q.val) > root.val:
            return self._get(root.right, p, q)
        elif max(p.val, q.val) < root.val:
            return self._get(root.left, p, q)
        else:
            return root

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node = self._get(root, p, q)
        assert node is not None
        return node