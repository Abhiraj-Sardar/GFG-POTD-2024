# A gallery with plants is divided into n parts, numbered 0, 1, 2, 3, ..., n-1. 
# There are provisions for attaching water sprinklers in every division. A sprinkler with range x at division i can water all divisions from i-x to i+x.

# Given an array gallery[] consisting of n integers, where gallery[i] is the range of the sprinkler at partition i (a power of -1 indicates no sprinkler attached), 
# return the minimum number of sprinklers that need to be turned on to water the entire gallery. If there is no possible way to water the full length using the given sprinklers, print -1.

# Example 1:

# Input:
# n = 6
# gallery[] = {-1, 2, 2, -1, 0, 0}
# Output:
# 2
# Explanation: 
# Sprinklers at index 2 and 5
# can water the full gallery, span of
# sprinkler at index 2 = [0,4] and span
# of sprinkler at index 5 = [5,5].
# Example 2:

# Input:
# n = 9
# gallery[ ] = {2, 3, 4, -1, 2, 0, 0, -1, 0}
# Output:
# -1
# Explanation: 
# No sprinkler can throw water
# at index 7. Hence all plants cannot be
# watered.
# Example 3:

# Input:
# n = 9
# gallery[ ] = {2, 3, 4, -1, 0, 0, 0, 0, 0}
# Output:
# 3
# Explanation: 
# Sprinkler at indexes 2, 7 and
# 8 together can water all plants.
# Your task:
# You do not have to take any input or print anything. Your task is to complete the function min_sprinklers() which takes the array gallery[ ] and the integer n as input parameters and returns the minimum number of sprinklers that need to be turned on to water the entire gallery.

# Expected Time Complexity: O( nlog(n) )
# Expected Auxiliary Space: O( n )

def min_sprinklers(self, arr, N):
    
    # Stores the leftmost and rightmost
    # point of every sprinklers
    V = []

    # Traverse the array arr[]
    for i in range(N):
        if (arr[i] > -1):
            V.append([i - arr[i], i + arr[i]])

    # Sort the array sprinklers in
    # ascending order by first element
    V.sort()

    # Stores the rightmost range
    # of a sprinkler
    maxRight = 0

    # Stores minimum sprinklers
    # to be turned on
    res = 0

    i = 0

    # Iterate until maxRight is
    # less than N
    while (maxRight < N):

        # If i is equal to V.size()
        # or V[i][0] is greater
        # than maxRight

        if (i == len(V) or V[i][0] > maxRight):
            return -1

        # Stores the rightmost boundary
        # of current sprinkler
        currMax = V[i][1]

        # Iterate until i+1 is less
        # than V.size() and V[i+1][0]
        # is less than or equal to maxRight
        while (i + 1 < len(V) and V[i + 1][0] <= maxRight):

            # Increment i by 1
            i += 1
            # Update currMax
        currMax = max(currMax, V[i][1])

    # If currMax is less than the maxRight
        if (currMax < maxRight):
            # Return -1
            return -1

        # Increment res by 1
        res += 1

        # Update maxRight
        maxRight = currMax + 1

        # Increment i by 1
        i += 1
    # Return res as answer
    return res
