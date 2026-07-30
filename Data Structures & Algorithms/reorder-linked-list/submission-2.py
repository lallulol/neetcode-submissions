# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return

        slow = head
        fast = head.next

        # Advance slow to the midpoint of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split: second half starts after slow, then disconnect the two halves
        second_half = slow.next
        slow.next = None

        first_half = head

        # Reverse second half
        curr, prev = second_half, None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        second_half = prev

        # Merge halves
        while first_half and second_half:
            first_next = first_half.next
            second_next = second_half.next

            first_half.next = second_half
            second_half.next = first_next

            first_half = first_next
            second_half = second_next