'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0])
        i, j = 0, (rows * columns) - 1

        while i <= j:
            mid = (i+j) >> 1
            mid_elements = matrix[mid // columns][mid % columns]
            if mid_elements == target:
                return True
            elif mid_elements < target:
                i = mid + 1
            else:
                j=mid -1
        return False
        
        
        
'''
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
'''
