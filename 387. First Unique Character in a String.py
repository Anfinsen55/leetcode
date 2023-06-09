'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic={}
        seen=set()
        for ind, let in enumerate(s):
            if let not in seen:
                dic[let]=ind
                seen.add(let)
            elif let in dic:
                del dic[let]
        return min(dic.values()) if dic else -1



'''
Example 1:

Input: s = "leetcode"
Output: 0
'''
