'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        low, high = 0, n - 1
        i = 0

        while i <= high:
            if nums[i] == 0:
                nums[low], nums[i] = nums[i], nums[low]
                low += 1
                i += 1
            elif nums[i] == 2:
                nums[high], nums[i] = nums[i], nums[high]
                high -= 1
            else:
                i += 1
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
'''
Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
'''
