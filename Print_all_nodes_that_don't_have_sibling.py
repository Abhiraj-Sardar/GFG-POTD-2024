# Print all nodes that don't have sibling

# Given a Binary Tree of n nodes, find all the nodes that don't have any siblings. 
# You need to return a list of integers containing all the nodes that don't have a 
# sibling in sorted order (Increasing).

# Two nodes are said to be siblings if they are present at the same level, 
# and their parents are the same.

# Note: The root node can not have a sibling so it cannot be included in our answer.

# Example 1:

# Input :
#        37
#       /   
#     20
#     /     
#   113 

# Output: 
# 20 113
# Explanation: 
# Nodes 20 and 113 dont have any siblings.

# Example 2:

# Input :
#        1
#       / \
#      2   3 

# Output: 
# -1
# Explanation: 
# Every node has a sibling.
# Your Task:  
# You don't need to read input or print anything. 
# Complete the function noSibling() which takes the 
# root of the tree as input parameter and returns a 
# list of integers containing all the nodes that don't 
# have a sibling in sorted order. If all nodes have a sibling, 
# then the returning list should contain only one element -1.

# Expected Time Complexity: O(nlogn)
# Expected Auxiliary Space: O(Height of the tree)

def noSibling(root):
    # code here
    result=[]
    
    def solve(root,result):
        
        if not root:
            return 
        
        if root.left is None and root.right is not None:
            result.append(root.right.data)
        elif root.left is not None and root.right is None:
            result.append(root.left.data)
        
        solve(root.left,result)
        solve(root.right,result)
    
    solve(root,result)
    
    if len(result)==0:
        return [-1]
    else:
        result.sort()
        
    return result