# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        arr=[]
        temp=head
        while temp is not None:
            gre=temp.next
            while gre is not None and gre.val<=temp.val:
                gre=gre.next
            if gre is not None:
                arr.append(gre.val)
            else:
                arr.append(0)
            temp=temp.next
        return arr

            


        
