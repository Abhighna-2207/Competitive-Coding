# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        first=temp.next
        second=first.next
        while second:
            c=0
            first=temp.next
            second=first.next
            while(first.val>0):
                c=c+first.val
                first=first.next
                second=second.next
            temp.val=c
            if second:
                temp.next=first
                temp=temp.next
        temp.next=None
        return head
