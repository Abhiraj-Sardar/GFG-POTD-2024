# Check if a number is divisible by 8

# Given a string representation of a decimal number s, check whether it is divisible by 8.

# Example 1:

# Input:
# s = "16"
# Output:
# 1
# Explanation:
# The given number is divisible by 8,
# so the driver code prints 1 as the output.
# Example 2:

# Input:
# s = "54141111648421214584416464555"
# Output:
# -1
# Explanation:
# Given Number is not divisible by 8, 
# so the driver code prints -1 as the output.
# Your Task:
# You don't need to read input or print anything.
# Your task is to complete the function DivisibleByEight()
# which takes a string s as the input and returns 1 if the
# number is divisible by 8, else it returns -1.

# Expected Time Complexity: O(1).
# Expected Auxillary Space: O(1).



class Solution:
    def DivisibleByEight(self,s):
        #code here
        n=len(s)
        if n>=3:
            a=s[-1]
            b=s[-2]
            c=s[-3]
            num=c+b+a
            num=int(num)
            if num%8==0:
                return 1
        
        else:
            num=int(s)
            if num%8==0:
                return 1
        
        return -1