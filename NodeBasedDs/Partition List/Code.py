# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if (not head) or (not head.next):
            return head
        if x>100 or x<-200:
            return head
        dl=ListNode('a')
        front=dl
        temp=head
        while (temp):
            if temp.val<x:
                newnode=ListNode(temp.val)
                dl.next=newnode
                dl=dl.next
            temp=temp.next
        temp=head
        while (temp):
            if temp.val>=x:
                newnode=ListNode(temp.val)
                dl.next=newnode
                dl=dl.next
            temp=temp.next
        temp=front
        front=temp.next
        return front
