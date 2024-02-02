# Implement Atoi

# Given a string, s, the objective is to convert it into 
# integer format without utilizing any built-in functions.
#  If the conversion is not feasible, the function should return -1.

# Note: Conversion is feasible only if all characters in the string 
# are numeric or if its first character is '-' and rest are numeric.

# Example 1:

# Input:
# s = "-123"
# Output: 
# -123
# Explanation:
# It is possible to convert -123 into an integer 
# and is so returned in the form of an integer
# Example 2:

# Input:
# s = "21a"
# Output: 
# -1
# Explanation: 
# The output is -1 as, due to the inclusion of 'a',
# the given string cannot be converted to an integer.
# Your Task:
# You do not have to take any input or print anything. 
# Complete the function atoi() which takes a string s as
#  an input parameter and returns an integer value representing 
# the given string. If the conversion is not feasible, the function should return -1.

# |s| = length of string str.
# Expected Time Complexity: O( |s| ), 
# Expected Auxiliary Space: O(1)


class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,s):
        res=0
        if s[0]=="-":
            if s[1:].isnumeric():
                for i in s[1:]:
                    z=ord("0")
                    r=ord(i)-z
                    res=res*10+r
                return (0-res)
            else:
                return -1
        elif s.isnumeric():
            for i in s:
                z=ord("0")
                r=ord(i)-z
                res=res*10+r
            return res
        else:
            return -1


            