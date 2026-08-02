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

        if (p.val < root.val < q.val) or (q.val < root.val < p.val) or p == root or q == root:
            return root

        left, right = self._get(root.left, p, q), self._get(root.right, p, q)
        if left is not None:
            return left
        elif right is not None:
            return right
        else:
            return None


    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node = self._get(root, p, q)
        assert node is not None
        return node

        