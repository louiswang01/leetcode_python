"""
Given two binary trees, write a function to check if they are equal or not. 
Two binary trees are considered equal if they are structurally identical and the nodes have the same value. 

Solution: recursively validate children nodes
"""

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            if p.val != q.val:
                return False
            return self.isSameTree(p.left, q.left) \
                and self.isSameTree(p.right, q.right)
        elif p or q:
            return False
        return True
