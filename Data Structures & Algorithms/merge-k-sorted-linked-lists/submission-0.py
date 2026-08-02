# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def merge(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        dummy = ListNode(0)
        new_list = dummy
        while list1 and list2:
            if list1.val < list2.val:
                new_list.next = list1
                list1 = list1.next
            else:
                new_list.next = list2
                list2 = list2.next
            new_list = new_list.next
        if list1:
            while list1:
                new_list.next = list1
                list1 = list1.next
                new_list = new_list.next
        else:
            while list2:
                new_list.next = list2
                list2 = list2.next
                new_list = new_list.next
        return dummy.next
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        while len(lists) > 1:
            merged = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                if i + 1 < len(lists):
                    l2 = lists[i + 1]
                else:
                    l2 = None
                merged.append(self.merge(l1, l2))
            lists = merged
        return lists[0]
        