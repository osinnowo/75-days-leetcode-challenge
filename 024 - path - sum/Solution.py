# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def count_paths(node, current_sum):
            if not node:
                return 0

            # Check the paths starting from the current node
            paths_from_current = count_paths_from_node(node, current_sum)

            # Check the paths in the left and right subtrees
            paths_from_left = count_paths(node.left, targetSum)
            paths_from_right = count_paths(node.right, targetSum)

            return paths_from_current + paths_from_left + paths_from_right

        def count_paths_from_node(node, current_sum):
            if not node:
                return 0

            # Check if the current node contributes to a valid path
            paths = 0
            if node.val == current_sum:
                paths += 1

            # Check paths in the left and right subtrees with updated sum
            paths += count_paths_from_node(node.left, current_sum - node.val)
            paths += count_paths_from_node(node.right, current_sum - node.val)

            return paths
        return count_paths(root, targetSum)
    


    
    


    








        