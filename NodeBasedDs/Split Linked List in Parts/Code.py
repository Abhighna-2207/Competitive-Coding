# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        def length(head):
            n=0
            temp=head
            while temp is not None:
                n=n+1
                temp=temp.next
            return n
        n=length(head)
        def distribution(m,k):
            arr=[0 for _ in range(k)]
            i=0
            while m>0:
                if i>=k:
                    i=0
                arr[i]+=1
                m-=1
                i=i+1
            return arr
        if k<n:
            dis=distribution(n,k)
        else:
            dis=[1 for _ in range(n)]
        ans=[]
        temp=head
        for i in range(len(dis)):
            front=temp
            for j in range(dis[i]-1):
                temp=temp.next
            y=temp.next
            temp.next=None
            ans.append(front)
            temp=y
        if k>n:
            for i in range(k-n):
                ans.append(None)
        return ans
        
                




        
        
