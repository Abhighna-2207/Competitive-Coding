class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def check(a,b):
            if a==sorted(b):
                return 0
            return -1
        n=len(s)
        m=len(p)
        res=[]
        p=sorted(p)
        for i in range(n-m+1):
            temp=s[i:i+m]
            if check(p,temp)==0:
                res.append(i)
        return res
                

        
