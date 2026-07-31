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
        dummy = Node(0)
        new_list = dummy
        ori_list = head
        copies = {}
        while ori_list:
            new_list.next = Node(ori_list.val)
            new_list = new_list.next
            copies[ori_list] = new_list
            ori_list = ori_list.next
        ori_list = head
        new_list = dummy.next
        while ori_list:
            if ori_list.random:
                new_list.random = copies[ori_list.random] 
            else:
                new_list.random = None
            ori_list = ori_list.next
            new_list = new_list.next
        
        return dummy.next
            