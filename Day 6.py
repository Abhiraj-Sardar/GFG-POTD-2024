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
