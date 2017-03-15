# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def ValidBST(self, root, mini, maxi):
        if root == None:
            return True
        if root.val < maxi and root.val > mini:
            return self.ValidBST(root.left, mini, root.val) and \
                   self.ValidBST(root.right, root.val, maxi)
        else:
            return False

    def isValidBST(self, root):
        return self.ValidBST(root, -sys.maxint - 1, sys.maxint)