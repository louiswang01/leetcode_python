"""
This is a math problem. Divisors of a number could appear in a pair
like (2,4) for 8, but also be a single number like 3 for 9. Because
bulb switching is a 2 status problem, light bulb will be off if it has
even number of divisors, vice versa. Therefore, we only need to count
the number of squre values no larger than n.
Simply we could put "return int(math.sqrt(n))".
"""

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=1
        while i**2 <=n:
            i+=1
        return i-1
