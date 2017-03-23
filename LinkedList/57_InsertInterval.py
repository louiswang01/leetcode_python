class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        result=[]
        newPosition=0
        for interval in intervals:
            if newInterval.start>interval.end:
                result.append(interval)
                newPosition+=1
            elif newInterval.end<interval.start:
                result.append(interval)
            else:
                newInterval.start=min(newInterval.start, interval.start)
                newInterval.end=max(newInterval.end, interval.end)
        result.insert(newPosition, newInterval)
        return result
