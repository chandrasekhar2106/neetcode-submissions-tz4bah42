# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        len_nodes = len(nodes)
        node_to_be_removed = len_nodes - n
        if node_to_be_removed == 0:
            head = head.next
        elif node_to_be_removed+1 < len_nodes:
            nodes[node_to_be_removed-1].next = nodes[node_to_be_removed+1]
        else:
            nodes[node_to_be_removed-1].next = None
        return head