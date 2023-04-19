#Given an integer x, return true if x is a palindrome , and false otherwise.

class Solution(object):
    def isPalindrome(self, x):
        x= str(x)
        return x ==x[::-1]



#Example 1:
#Input: x = 121
#Output: true
#Explanation: 121 reads as 121 from left to right and from right to left.
