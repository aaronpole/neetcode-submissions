# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find Middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Found the middle so we're cutting off connections
        second = slow.next
        slow.next = None

        # Reverse second list
        prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node
        
        # Merge the both halves alternatively
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2


        