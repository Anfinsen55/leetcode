'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = nums[0],1
        for i in range(1, len(nums)):
            if nums[i] == res: count += 1
            else:
                if count == 0: res,count = nums[i],1
                count -= 1
        return res
      
      
'''
Example 1:

Input: nums = [3,2,3]
Output: 3
'''
