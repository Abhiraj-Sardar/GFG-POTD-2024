# LCS of three strings

# Given 3 strings A, B and C, the task is to find the 
# length of the longest sub-sequence that is common in all the three given strings.

# Example 1:

# Input:
# A = "geeks"
# B = "geeksfor", 
# C = "geeksforgeeks"
# Output: 5
# Explanation: 
# "geeks"is the longest common
# subsequence with length 5.
# Example 2:

# Input: 
# A = "abcd"
# B = "efgh"
# C = "ijkl"
# Output: 0
# Explanation: 
# There's no subsequence common
# in all the three strings.
# Your Task:
# You don't need to read input or print anything. 
# Your task is to complete the function LCSof3() which 
# takes the strings A, B, C and their lengths n1, n2, n3 as input 
# and returns the length of the longest common subsequence in all the 3 strings.

# Expected Time Complexity: O(n1*n2*n3).
# Expected Auxiliary Space: O(n1*n2*n3).

class Solution:

    def LCSof3(self,X, Y, Z, m, n, o):
        L = [[[0 for i in range(o+1)] for j in range(n+1)]
         for k in range(m+1)]
 
   
        for i in range(m+1):
            for j in range(n+1):
                for k in range(o+1):
                    if (i == 0 or j == 0 or k == 0):
                        L[i][j][k] = 0
                         
                    elif (X[i-1] == Y[j-1] and
                          X[i-1] == Z[k-1]):
                        L[i][j][k] = L[i-1][j-1][k-1] + 1
     
                    else:
                        L[i][j][k] = max(max(L[i-1][j][k],
                        L[i][j-1][k]),
                                        L[i][j][k-1])
     
       
        return L[m][n][o]
        
        
