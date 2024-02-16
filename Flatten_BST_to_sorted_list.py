# Flatten BST to sorted list

# You are given a Binary Search Tree (BST) with n nodes, 
# each node has a distinct value assigned to it. The goal
#  is to flatten the tree such that, the left child of each 
#  element points to nothing (NULL), and the right child points to the 
#  next element in the sorted list of elements of the BST (look at the examples for clarity). 
#  You must accomplish this without using any extra storage, except for recursive calls, which are allowed.

# Note: If your BST does have a left child, then the system will print a -1 and will skip it, 
# resulting in an incorrect solution.

# Example 1:

# Input:
#           5
#         /    \
#        3      7
#       /  \    /   \
#      2   4  6     8
# Output: 2 3 4 5 6 7 8
# Explanation: 
# After flattening, the tree looks
# like this
#     2
#      \
#       3
#        \
#         4
#          \
#           5
#            \
#             6
#              \
#               7
#                \
#                 8
# Here, left of each node points
# to NULL and right contains the
# next node.
# Example 2:

# Input:
#        5
#         \
#          8
#        /   \
#       7     9  
# Output: 5 7 8 9
# Explanation:
# After flattening, the tree looks like this:
#    5
#     \
#      7
#       \
#        8
#         \
#          9
# Your Task:
# You don't need to read input or print anything. 
# Your task is to complete the function flattenBST() 
# which takes root node of the BST as input parameter
#  and returns the root node after transforming the tree.

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(N)


class Solution:
    
    def flatten(self,pos,prev,sorted_list):
        
        if pos==len(sorted_list):
            return
        prev[0].right=Node(sorted_list[pos])
        prev[0].left=None
        prev[0]=prev[0].right
        self.flatten(pos+1,prev,sorted_list)
    
    def inorder(self,curr,sorted_list):
        if curr is None:
            return 
        self.inorder(curr.left,sorted_list)
        sorted_list.append(curr.data)
        self.inorder(curr.right,sorted_list)
    
    def flattenBST(self, root):
        sorted_list=[]
        curr=root
        self.inorder(curr,sorted_list)
        dummy=Node(-1)
        prev=[dummy]
        self.flatten(0,prev,sorted_list)
        prev[0].right=None
        prev[0].left=None
        result=dummy.right
        dummy=None
        return result
