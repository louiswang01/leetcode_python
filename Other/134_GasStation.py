"""
when loop through the gas stations:
    1. if current sum<0, previous stations will not be the start point
    2. if total sum>0, there should be a valid start point
    (use induction to prove)
"""

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
        if len(gas)==0:
            return 0
        
        currStart=0
        currLeft=0
        totalLeft=0
        for i in range(len(gas)):
            tempLeft=gas[i]-cost[i]
            totalLeft+=tempLeft
            if currLeft+tempLeft>=0:
                currLeft+=tempLeft
            else:
                currStart=i+1
                currLeft=0
        if currStart>=len(gas) or totalLeft<0:
            return -1
        return currStart
        
