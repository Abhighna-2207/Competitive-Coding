class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s=str(num)
        i=0
        j=k
        n=len(s)
        c=0
        while(j<=n):
            temp=int(s[i:j])
            if temp>0 and num%temp==0:
                c+=1
            i+=1
            j=j+1
        return c
        

        
