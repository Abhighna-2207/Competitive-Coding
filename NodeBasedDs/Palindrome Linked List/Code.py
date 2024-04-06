class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        temp=head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        l=0
        r =len(arr) - 1
        while l < r and arr[l] == arr[r]:
            l += 1
            r -= 1
        return l >= r
