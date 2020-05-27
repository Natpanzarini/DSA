# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # Brute force: go through list to count number of nodes
            # divide length by 2
            # return the node at the half position

        #Better solution:
            # Fast/slow pointer:
                # Increment fast pointer by 2, slow pointer by 1
                # When fast pointer reaches the end, if there are no more nodes to increment, return node at slow
                # when fast pointer reaches the end, if there is only one more node to increment, return node at slow + 1

        #Runtime: O(n) - 32ms, 39.78%
        #Space: O(1) - 13.8mb, 7.14%

        fast = head
        slow = head

        while(fast.next != None):
            fast = fast.next
            if fast.next == None:
                return slow.next
            fast = fast.next
            slow = slow.next

        return slow
