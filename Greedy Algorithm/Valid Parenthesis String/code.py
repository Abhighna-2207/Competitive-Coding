class Solution:
    def checkValidString(self, s: str) -> bool:
        if s=="":
            return True
        if s[-1]=="(" or s[0]==")" or s[0]==")" or s[-1]=="(":
            return False
        stack=[]
        n=len(s)
        i=0
        for i in range(n):
            if s[i]=="(" or s[i]=="*":
                stack.append(s[i])
            elif s[i]==")":
                j=len(stack)-1
                if j==-1:
                    return False
                while j>0 and stack[j]!="(":
                    j-=1
                print(stack,stack[j])
                if stack[j]=="*" or stack[j]=="(":
                    stack.pop(j)
            print(stack)
        count=stack.count("(")
        if count==0:
            return True
        if stack[-1]=="(":
            return False
        i=len(stack)-1
        while count>0:
            if len(stack)>0 and stack[-1]=="(":
                return False
            while i>0 and stack[i]!="(":
                i-=1
            if stack[i+1]=="*":
                stack.pop(i)
                stack.pop(i)
                count-=1
            if i>=len(stack):
                i=len(stack)-1
        return True
