# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.doInorderTraversal(root,[])
       
    def doInorderTraversal(self, root, vals):
        if root == None:
            return vals
        
        vals=self.doInorderTraversal(root.left, vals)
        vals.append(root.val)
        vals=self.doInorderTraversal(root.right, vals)
        return vals
