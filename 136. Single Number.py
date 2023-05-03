'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once = 0
        for i in nums:
            once ^=i
        return once
      
'''
Example 1:

Input: nums = [2,2,1]
Output: 1
'''
