'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def find_depth(node,l):
            if node is None:
                return l

            l += 1

            return max(find_depth(node.left,l),find_depth(node.right,l))
        return find_depth(root,0)
        
        
'''
Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
'''
