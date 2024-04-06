# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next==None:
            return head
        temp=head
        n=0
        if temp.next:
            temp=temp.next
            mid=temp
        while temp.next:
            temp=temp.next
            if temp.next:
                temp=temp.next
                mid=mid.next
        return mid
