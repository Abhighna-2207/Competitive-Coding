# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if not head:
            return 0
        def size(head):
            if not head:
                return 0
            n=0
            temp=head
            while temp:
                temp=temp.next
                n=n+1
            return n
        temp=head
        l=size(temp)-1
        num=0
        while l>-1:
            num+=temp.val*(2**(l))
            l=l-1
            temp=temp.next
        return num
        
