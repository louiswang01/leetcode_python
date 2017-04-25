"""
* Bitwise operation
This XOR operation works because it's like XORing all the numbers by itself.And it is commutative.
So if the array is {2,1,4,5,2,4,1} then it will be like we are performing this operation

((2^2)^(1^1)^(4^4)^(5)) => (0^0^0^5) => 5.

Hence picking the odd one out ( 5 in this case).

"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        result = 0
        for num in nums:
            result ^= num
        return result
