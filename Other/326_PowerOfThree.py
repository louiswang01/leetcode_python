"""
Given an integer, write a function to determine if it is a power of three. 

O(1) solution:
    1162261467 is 3^19,  3^20 is bigger than int
"""

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 1162261467 % n == 0
