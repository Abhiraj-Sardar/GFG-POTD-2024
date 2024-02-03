# Decimal Equivalent of Binary Linked List

# Given a singly linked list of length n. The link list represents a binary number, 
# ie- it contains only 0s and 1s. Find its decimal equivalent.
# The significance of the bits decreases with the increasing index in the linked list.
# An empty linked list is considered to represent the decimal value 0. 

# Since the answer can be very large, answer modulo 109+7 should be printed.

# Example 1:
# Input:
# n = 3
# Linked List = {0, 1, 1}
# Output:
# 3
# Explanation:
# 0*22 + 1*21 + 1*20 =  1 + 2 + 0 = 3
# Example 2:
# Input:
# n = 4
# Linked List = {1, 1, 1, 0}
# Output:
# 14
# Explanation:
# 1*23 + 1*22 + 1*21 + 0*20 =  8 + 4 + 2 + 0 = 14
# Your Task:
# You do not have to take any input or print anything. 
# Complete the function decimalValue() which takes a head 
# node of a linked list as an input parameter and returns decimal
#  representation of it.

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)

class Solution:
    def decimalValue(self, head):
        MOD=10**9+7
        res=0
        length=0
        if head is None:
            return 0
        else:
            current=head
            while current:
                length+=1
                current=current.next
                
            current=head
            power=length-1
            while current and power>=0:
                data=current.data
                base=(2**power)%MOD
                data=(data*base)%MOD
                res=(res+data)%MOD
                current=current.next
                power-=1
            return res
                

