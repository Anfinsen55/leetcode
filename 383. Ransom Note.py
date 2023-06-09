'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        string1, string2 = Counter(ransomNote), Counter(magazine)
        if string1 & string2 == string1:
            return True
        return False
        
        
'''
Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
'''
