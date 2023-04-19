#Given an integer array nums, find the subarray with the largest sum, and return its sum.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_len= float('-inf')
        max_value=0

        for num in nums:
            max_value += num
            max_len = max(max_len, max_value)
            max_value = max(max_value, 0)
        return max_len
        
        
#Example 1:
#Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#Output: 6
#Explanation: The subarray [4,-1,2,1] has the largest sum 6.
