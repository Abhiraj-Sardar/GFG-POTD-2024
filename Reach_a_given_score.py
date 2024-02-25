# Reach a given score

# Consider a game where a player can score 3 or 5 or 10 points in a move.
# Given a total score n, find number of distinct combinations to reach 
# the given score.

# Example 1:

# Input
# n = 10
# Output
# 2
# Explanation
# There are two ways {5,5} and {10}.
# Example 2:

# Input
# n = 20
# Output
# 4
# Explanation
# There are four possible ways. {5,5,5,5}, {3,3,3,3,3,5}, {10,10}, {5,5,10}.
# Your Task:  
# You don't need to read input or print anything. Your task is to complete 
# the function count( ) which takes n as input parameter and returns the 
# answer to the problem.

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(n)

class Solution:
    def count(self, n: int) -> int:
        table=[0 for _ in range(n+1)]
        table[0]=1
        
        for i in range(3, n+1):
            table[i] += table[i-3]
        for i in range(5, n+1):
            table[i] += table[i-5]
        for i in range(10, n+1):
            table[i] += table[i-10]
 
        
        return table[n]
            
        

