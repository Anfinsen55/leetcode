'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        stack = [(root)]
        a = []
        while stack:
            lvl = []
            for i in range(len(stack)):
                n= stack.pop(0)
                lvl.append(n.val)
                if n.left: stack.append(n.left)
                if n.right: stack.append(n.right)

            a.append(lvl)
        return a
        
        
        
'''
Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
'''
