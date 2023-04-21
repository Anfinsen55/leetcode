'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
        
        
'''
Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
'''
#secondary output

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l,n=0,0
        s+=' '
        for i in range(len(s)):
            if s[i]!=' ':
                n+=1
            else:
                if n>0:
                    l=n   
                n=0
        return l         
