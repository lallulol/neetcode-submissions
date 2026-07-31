# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        new_list = dummy
        while l1 or l2 or carry:
            total=0
            if l1:
                total+=l1.val
                l1 = l1.next
            if l2:
                total+=l2.val
                l2 = l2.next
            total+=carry
            
            number = total%10
            carry = total//10
            new_list.next = ListNode(number)
            new_list = new_list.next
        return dummy.next