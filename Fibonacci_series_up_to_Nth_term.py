# Fibonacci series up to Nth term

# You are given an integer n, return the fibonacci series till the nth(0-based indexing) term. 
# Since the terms can become very large return the terms modulo 109+7.

# Example 1:

# Input:
# n = 5
# Output:
# 0 1 1 2 3 5
# Explanation:
# 0 1 1 2 3 5 is the Fibonacci series up to the 5th term.
# Example 2:

# Input:
# n = 10
# Output:
# 0 1 1 2 3 5 8 13 21 34 55
# Explanation:
# 0 1 1 2 3 5 8 13 21 34 55 is the Fibonacci series up to the 10th term.
# Your Task:
# You don't need to read input or print anything. 
# Your task is to complete the function Series() 
# which takes an Integer n as input and returns a Fibonacci 
# series up to the nth term.

# Expected Time Complexity: O(n)
# Expected Space Complexity: O(n)


class Solution:
    def series(self, n):
        MOD=1000000007
        result=[0,1]
        a=result[0]
        b=result[1]
        for i in range(1,n):
            c=((a%MOD)+(b%MOD))%MOD
            result.append(c)
            a=result[i]
            b=result[i+1]
        return result
