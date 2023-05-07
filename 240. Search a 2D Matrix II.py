'''
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,col=len(matrix),len(matrix[0])
        for row in matrix:
            left,right=0,len(row)-1
            while left<=right:
                mid=(left+right)//2
                if row[mid]==target:
                    return True
                if row[mid]>target:
                    right=mid-1
                else:
                    left=mid+1
        return False
      
      
      
'''
Example 1:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
'''
