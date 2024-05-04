class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s)<3:
            return 0
        n=len(s)
        c=0
        for i in range(n-2):
            if s[i]==s[i+1] or s[i+1]==s[i+2] or s[i]==s[i+2]:
                continue
            c+=1
        return c 
