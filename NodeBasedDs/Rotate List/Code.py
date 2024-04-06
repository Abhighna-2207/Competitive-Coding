# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if (k==0) or (not head) or (not head.next):
            return head
        def check():
            temp=head
            i=0
            while temp.next:
                temp=temp.next
                i=i+1
            return i+1
        t=check()
        if t<k:
            k=k%t
        def sol(head,k):
            a=head
            i=0
            while i<k:
                while a.next.next:
                    a=a.next
                b=a.next
                b.next=head
                a.next=None
                head=b
                a=head
                i+=1
            return head
        return sol(head,k)
