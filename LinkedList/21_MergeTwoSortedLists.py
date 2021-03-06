"""
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l = ListNode(0)
        head = l
        
        while l1 and l2:    # concise style
            if l1.val > l2.val:
                l.next = l2
                l2 = l2.next
            else:
                l.next = l1
                l1 = l1.next
            l = l.next      # do forget to move l listNode
        
        if l1 == None:
            l.next = l2
        else:
            l.next = l1
        
        return head.next    # skip empty head node
