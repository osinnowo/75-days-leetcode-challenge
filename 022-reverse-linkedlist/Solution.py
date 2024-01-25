from typing import Optional
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head 
        previous = None
        while(node is not None):
            next = node.next
            node.next = previous
            previous = node
            node = next
        return previous
        