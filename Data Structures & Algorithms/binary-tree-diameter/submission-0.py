# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    _max_depth: int

    def __init__(self):
        self._max_depth = 0

    def _node_depth(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        return 1 + max(self._node_depth(node.right), self._node_depth(node.left))

    def _diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        diameter = self._node_depth(root.left) + self._node_depth(root.right)
        print(f'{root.val=}, {diameter=}')
        return diameter
            
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        diameter: int = self._diameterOfBinaryTree(root)

        return max(diameter, self.diameterOfBinaryTree(root.right), self.diameterOfBinaryTree(root.left))
        