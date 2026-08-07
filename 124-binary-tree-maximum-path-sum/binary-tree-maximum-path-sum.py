# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize as a single-element list to allow mutation inside dfs
        res = [root.val]

        def dfs(node):
            if not node:
                return 0

            # Compute maximum path sum from left and right subtrees
            # Clamp negative subtree sums to 0 (ignoring bad paths)
            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)

            # Update maximum path sum including the current node as the "split point"
            res[0] = max(res[0], node.val + leftMax + rightMax)

            # Return max path sum that can be extended to the parent (no split)
            return node.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]