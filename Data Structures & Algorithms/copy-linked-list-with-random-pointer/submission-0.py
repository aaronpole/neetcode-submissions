"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        curr = head
        mp = {}

        while curr:
            mp[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            if curr.next:
                mp[curr].next = mp[curr.next]
            else:
                mp[curr].next = None
            if curr.random:
                mp[curr].random = mp[curr.random]
            else:
                mp[curr].random = None
            curr = curr.next
        return mp[head]
