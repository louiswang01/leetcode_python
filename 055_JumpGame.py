"""
Given an array of non-negative integers, you are initially positioned at the first index of the array. 
Each element in the array represents your maximum jump length at that position. 
Determine if you are able to reach the last index. 

For example:
A = [2,3,1,1,4], return true. 
A = [3,2,1,0,4], return false. 

------------------------------------------------------
Solution: 
As the element represents the maximum jump, it means that it will be very slow and complex to consider a specific route.

Method 1:
A more efficient way to solve this is to find "zero gaps" and decide whether it could be jumped over by looping from the end of array.

Method 2:
Another way is to loop from the start of array and record the max steps left. The max step left is calculated by jump[i] = max(jump[i-1], nums[i-1]) -1. When the max step is smaller than 0, than return false. 
Also, it could be written as Greedy.

Method 3:
DP is usable here. Though it's slow.
"""

# Method 1
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<=1:
            return True
            
        p=len(nums)-2   # start from the (n-1)th element
        zero_gap=0
        while p>=0:     # loop from the end of array
            if nums[p]>zero_gap:    # current zero gap could be jumped over
                zero_gap=0
            else:
                zero_gap+=1         # if not, gap grows by 1
            p-=1
        if zero_gap>0:
            return False
        return True
