# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None

        while head:

            tmp = head.next     # head.next will be None by default if DNE
            head.next = prev

            prev = head
            head = tmp

        return prev             # head will be None, prev now points to LL start

        # n = length of LL
        # Time Complexity: = O(n)
        # Space Complexity: O(1)