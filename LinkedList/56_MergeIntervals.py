# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

"""
1. sort on start values
2. loop and merge
"""
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals==[]:
            return intervals
        intervals=sorted(intervals, key=lambda x: x.start)
        merged=[]
        for interval in intervals:
            if merged==[] or interval.start>merged[-1].end:
                # python evaluate or lazily
                merged.append(interval)
            else:
                merged[-1].end=max(interval.end,merged[-1].end)
        return merged
