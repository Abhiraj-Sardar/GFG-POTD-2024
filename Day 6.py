# Top k numbers in a stream

# Given N numbers in an array, your task is to keep at most the top K numbers with respect to their frequency.

# In other words, you have to iterate over the array, and after each index, determine the top K most frequent numbers until that
#  iteration and store them in an array in decreasing order of frequency. An array will be formed for
#  each iteration and stored in an array of arrays. If the total number of distinct elements is less than K, 
# then keep all the distinct numbers in the array. If two numbers have equal frequency, place the smaller number 
# first in the array.

# Example 1:

# Input:
# N=5, K=4
# arr[] = {5, 2, 1, 3, 2} 
# Output: 
# 5 
# 2 5 
# 1 2 5 
# 1 2 3 5 
# 2 1 3 5 
# Explanation:
# Firstly there was 5 whose frequency
# is max till now. So resulting sequence is {5}.
# Then came 2, which is smaller than 5 but
# their frequencies are same so resulting sequence is {2, 5}.
# Then came 1, which is the smallest among all the
# numbers arrived, so resulting sequence is {1, 2, 5}.
# Then came 3 , so resulting sequence is {1, 2, 3, 5}
# Then again 2, which has the highest
# frequency among all numbers, 
# so resulting sequence {2, 1, 3, 5}.
# Example 2:

# Input:
# N=6, K=3
# arr[] = {2, 1, 2, 1, 2, 1} 
# Output: 
# 2 
# 1 2 
# 2 1 
# 1 2 
# 2 1
# 1 2
# Explanation:
# As total number of distinct values never
# exceeds 2, you have to return only those two
# values. In the case where frequency of 1 gets
# equal with the frequency of 2, you have to 
# keep 1 before 2 in the array.
# Your Task:
# Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function kTop() that takes array a, integer n and integer k as parameters and returns the array of arrays.

# Expected Time Complexity: O(N*K).
# Expected Auxiliary Space: O(N).



class Solution:
    def kTop(self,a, N, K):
        result=[]
        temp=[0 for _ in range(K+1)]
        freq={i:0 for i in range(K+1)}
    
        for i in range(N):
            if a[i] in freq.keys():
                freq[a[i]]+=1
            else:
                freq[a[i]]=1
            
            temp[K]=a[i]
            pos=temp.index(a[i])
            pos=pos-1
            while pos>=0:
                if (freq[temp[pos]]<freq[temp[pos+1]]):
                    t=temp[pos]
                    temp[pos]=temp[pos+1]
                    temp[pos+1]=t
                elif ((freq[temp[pos]]==freq[temp[pos+1]]) and (temp[pos+1]<temp[pos])):
                    t=temp[pos]
                    temp[pos]=temp[pos+1]
                    temp[pos+1]=t
                else:
                    break
                pos-=1
            pos=0
            array=[]
            for x in range(i+1):
                if x==K:
                    break
                if temp[x]==0:
                    continue
                array.append(temp[x])
            result.append(array)
            array=None
        return result
