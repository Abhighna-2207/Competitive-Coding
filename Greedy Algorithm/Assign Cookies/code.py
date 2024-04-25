class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        c=0
        i=0
        j=0
        lg=len(g)
        ls=len(s)
        g.sort()
        s.sort()
        while i<lg and j<ls:
            if s[j]>=g[i]:
                c+=1
                i+=1
            j+=1
        return c

        
