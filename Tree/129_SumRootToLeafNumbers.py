"""
Tree Traversal + number memory
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def preOrderTraversal(root,val,lst):
            val=val*10+root.val
            if root.left==None and root.right==None:
                lst.append(val)
                return lst
            if root.left:
                lst=preOrderTraversal(root.left,val,lst)
            if root.right:
                lst=preOrderTraversal(root.right,val,lst)
            return lst
        
        if root==None:
            return 0
        val=0
        lst=[]
        lst=preOrderTraversal(root,val,lst)
        return sum(lst)
