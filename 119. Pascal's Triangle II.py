'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
'''

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(1, rowIndex+1):
            element = row[-1] * (rowIndex-i+1) // i
            row.append(element)
        return row
      
      
      
      
'''
Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
'''
