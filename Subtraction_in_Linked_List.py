# Subtraction in Linked List

# You are given two linked lists that represent two large positive numbers.
# From the two numbers represented by the linked lists, subtract the smaller
# number from the larger one. Look at the examples to get a better understanding 
# of the task.

# Example 1:

# Input:
# L1 = 1->0->0
# L2 = 1->2
# Output: 88
# Explanation:  
# First linked list represents 100 and the
# second one represents 12. 12 subtracted from 100
# gives us 88 as the result. It is represented
# as 8->8 in the linked list.
# Example 2:

# Input:
# L1 = 0->0->6->3
# L2 = 7->1->0
# Output: 647
# Explanation: 
# First linked list represents 0063 => 63 and 
# the second one represents 710. 63 subtracted 
# from 710 gives us 647 as the result. It is
# represented as 6->4->7 in the linked list.
# Your Task:
# You do not have to take any input or print anything. 
# The task is to complete the function subLinkedList() 
# that takes heads of two linked lists as input parameters
# and which should subtract the smaller number from the larger 
# one represented by the given linked lists and return the head 
# of the linked list representing the result.

# n and m are the length of the two linked lists respectively.
# Expected Time Complexity:  O(n+m)
# Expected Auxiliary Space: O(n+m)


class Solution:
    def subLinkedList(self, l1, l2): 
        maximum=0
        minimum=0
        num1,num2=0,0
        current=l1
        head=None
        ptr=None

        while current:
            r=current.data
            num1=num1*10+r
            current=current.next
            
        current=l2
        
        while current:
            r=current.data
            num2=num2*10+r
            current=current.next
        
        if num1<num2:
            minimum=num1
            maximum=num2
        elif num1>num2:
            minimum=num2
            maximum=num1
        else:
            minimum=num1
            maximum=num2
            
        result=maximum-minimum
        result=str(result)
        for i in result:
            if head is None:
                ptr=Node(int(i))
                head=ptr
            else:
                ptr.next=Node(int(i))
                ptr=ptr.next
                
        return head
        

