"""209. Minimum Size Subarray Sum
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        sum_subarray=0
        min_length = float('inf')
        for right in range(len(nums)):
            sum_subarray += nums[right]

            while sum_subarray >= target:
                min_length = min(min_length, right-left+1)
                sum_subarray -= nums[left]
                left += 1

        if min_length == float('inf'):
            return 0

        return min_length

