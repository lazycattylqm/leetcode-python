from src.leetcode.tree_node import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodesRecursive(root, root.val)

    def goodNodesRecursive(self, root: TreeNode, maxVal: int) -> int:
        if root is None:
            return 0

        goodNodes = 0
        if root.val >= maxVal:
            goodNodes += 1

        maxVal = max(maxVal, root.val)
        goodNodes += self.goodNodesRecursive(root.left, maxVal)
        goodNodes += self.goodNodesRecursive(root.right, maxVal)

        return goodNodes
