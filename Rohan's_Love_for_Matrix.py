# Rohan's Love for Matrix

# Rohan has a special love for the matrices especially for the 
# first element of the matrix. Being good at Mathematics, he also
# loves to solve the different problem on the matrices. So one day he started 
# to multiply the matrix with the original matrix.  The elements of the original 
# matrix a are given by [a00=1 , a01=1, a10=1, a11=0].
# Given the power of the matrix, n calculate the an and return the a10 element mod 1000000007.

# Example 1:

# Input: 
# n = 3
# Output: 
# 2 
# Explanation: Take the cube of the original matrix 
# i.e a3 and the (a10)th element is 2.
# Example 2:

# Input: 
# n = 4
# Output: 
# 3
# Explanation: Take the cube of the original matrix 
# i.e a4 and the (a10)th element is 3.
# Your Task:  
# You dont need to read input or print anything. Complete 
# the function firstElement() which takes n as input parameter 
# and returns the a10 element mod 1000000007 of an.

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)


class Solution:
    def firstElement (self, n):
        # code here
        # MOD=1000000007
        
        # A00=(1*1)+(1*1)
        # A01=(1*1)+(1*0)
        # A10=(1*1)+(0*1)
        # A11=(1*1)+(0*0)
        
        # B=[[A00,A01],[A10,A11]]
        
        # for i in range(n-2):
        #     A00=((B[0][0]*1)%MOD+(B[0][1]*1)%MOD)%MOD
        #     A01=((B[0][0]*1)%MOD+(B[0][1]*0)%MOD)%MOD
        #     A10=((B[1][0]*1)%MOD+(B[1][1]*1)%MOD)%MOD
        #     A11=((B[1][0]*1)%MOD+(B[1][1]*0)%MOD)%MOD
            
        #     B[0][0]=A00%MOD
        #     B[0][1]=A01%MOD
        #     B[1][0]=A10%MOD
        #     B[1][1]=A11%MOD
            
        # return B[1][0]%MOD
        
        
        MOD=1000000007
        a=1
        b=1
        c=(a+b)%MOD
        
        if n==0 or n==1:return 1
        
        for i in range(n-2):
            c=(a+b)%MOD
            a=b%MOD
            b=c%MOD
            
        return c
