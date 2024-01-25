# Shortest Prime Path

# You are given two four digit prime numbers num1 and num2. 
# Find the distance of the shortest path from Num1 to Num2 that
#  can be attained by altering only single digit at a time such 
#  that every number that we get after changing a digit is a four 
#  digit prime number with no leading zeros.

# Example 1:

# Input:
# num1 = 1033 
# num2 = 8179
# Output: 6
# Explanation:
# 1033 -> 1733 -> 3733 -> 3739 -> 3779 -> 8779 -> 8179.
# There are only 6 steps reuired to reach num2 from num1. 
# and all the intermediate numbers are 4 digit prime numbers.
# Example 2:

# Input:
# num1 = 1033 
# num2 = 1033
# Output:
# 0
# Your Task:  
# You don't need to read input or print anything. 
# Your task is to complete the function solve() 
# which takes two integers num1 and num2 as input 
# parameters and returns the distance of the shortest
#  path from num1 to num2. If it is unreachable then return -1.

# Expected Time Complexity: O(nlogn)
# Expected Auxiliary Space: O(n)


class Solution:
    def solve (self,Num1,Num2):
        max_num = 9999
        prime = [1]*10001
        prime[1] = 0
        for i in range(2, int(max_num**0.5) + 1):
            if prime[i]:
                for j in range(i*i, max_num + 1, i):
                    prime[j] = 0
        dp = [-1] * 10001
        vis = [0] * 10001
        q = []
        q.append(Num1)
        dp[Num1] = 0
        vis[Num1] = 0
        while q:
            current = q.pop(0)
            if vis[current]:
               continue
            vis[current] = 1
            s = str(current)
            for i in range(4):
                for ch in range(10):
                    ch = str(ch)
                    if ch == s[i] or (ch == '0' and i == 0): 
                        continue
                    next = list(s)
                    next[i] = ch
                    next_num = int(''.join(next))
                    if prime[next_num] and dp[next_num] == -1:
                        dp[next_num] = 1 + dp[current]
                        q.append(next_num)
                    if next_num == Num2:
                        return dp[next_num]
        return dp[Num2]




