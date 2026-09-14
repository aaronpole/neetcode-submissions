# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        temphead = ListNode(0)
        temp = temphead
        while l1 or l2 or carry != 0:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = x + y + carry
            carry = sum//10
            newNode = ListNode(sum%10)
            temp.next = newNode
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            temp = temp.next
        return temphead.next
        