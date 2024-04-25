class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        count=1
        i=1
        prev=pairs[0][1]
        n=len(pairs)
        while i<n:
            if prev<pairs[i][0]:
                prev=pairs[i][1]
                count+=1
            i+=1
        return count
        
