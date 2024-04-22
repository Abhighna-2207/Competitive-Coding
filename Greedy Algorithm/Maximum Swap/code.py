class Solution:
    def maximumSwap(self, num: int) -> int:
        n=[int(x) for x in str(num)]
        i=0
        l=len(n)
        while i<l-1:
            maxx=max(n[i+1:])
            if n[i]<maxx:
                j=l-1
                while j>i and n[j]!=maxx:
                    j-=1
                n[i],n[j]=n[j],n[i]
                break
            else:
                i+=1
        s=0
        for i in n:
            s=s*10+i
        return s
        
