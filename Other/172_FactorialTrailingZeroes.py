"""
Essentially, we just need to count the number of 5 in the factorial. But this is not enough.
As we know, do n/5 we got the number of values that has 5 as their factor while n/5/5 is the number of values that has 5*5 as their factor.
In light of this we need to loop the division until the quotient becomes smaller than 1. 
"""

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        fives=0
        quotient=n
        while quotient>0:
            quotient/=5
            fives+=quotient
        return fives
