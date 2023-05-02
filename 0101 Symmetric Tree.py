'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def solve(root1,root2):
            if not root1 and not root2:
                return True

            if not root1 or not root2:
                return False

            return root1.val== root2.val and solve(root1.left,root2.right) and solve(root1.right,root2.left)

        return solve(root.left,root.right) 
        
        
        
'''
Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
'''
