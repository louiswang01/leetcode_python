class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None or k==0:
            return head
        l1=head
        i=1
        while head.next:
            head=head.next
            i+=1
        head.next=l1
        
        k1=k%i
        for j in range(i-k1-1):
            l1=l1.next
        new_head=l1.next
        l1.next=None
        return new_head