# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time complexity: O(nklogk)
# Space complexity: O(k)

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        # create a heap
        heap = []
        for node in lists:
            if node:
                # store (priority, task) tuples on the heap to 'heapify'
                heap.append((node.val, node))
        heapq.heapify(heap)
        
        head = ListNode(0)
        l = head
        
        while heap:
            nextNode = heapq.heappop(heap)
            l.next = ListNode(nextNode[0])
            l = l.next
            if nextNode[1].next:
                heapq.heappush(heap, (nextNode[1].next.val, nextNode[1].next))
        
        return head.next
        
     
