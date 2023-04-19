#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

class Solution(object):
    def romanToInt(self, s):
        roman={"I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000}
        sum=0
        for i in range(len(s)-1):
            if roman[s[i]]< roman[s[i+1]]:
                sum -= roman[s[i]]
            else:
                sum += roman[s[i]]
        return sum + roman[s[-1]]



#Example 1:
#Input: s = "III"
#Output: 3
#Explanation: III = 3.
