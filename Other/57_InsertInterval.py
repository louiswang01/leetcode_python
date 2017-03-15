# This solution is inefficient.. Need a second try

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """

        if len(intervals) == 0:
            return [newInterval]

        # construct interval dictionary
        d = {}
        itvs1 = []
        itvs2 = []
        intervals.append(newInterval)
        for itv in intervals:
            if itv.start > newInterval.end:
                itvs2.append(itv)
            elif itv.end < newInterval.start:
                itvs1.append(itv)
            else:
                if not itv.start in d:
                    d[itv.start] = itv.end
                else:
                    if itv.end > d[itv.start]:
                        d[itv.start] = itv.end

        # merge
        newItvs = []
        temp = None
        for left in sorted(d.iterkeys()):
            if temp == None:
                temp = Interval(left, d[left])
            else:
                if left <= temp.end:
                    if d[left] > temp.end:
                        temp = Interval(temp.start, d[left])
                else:
                    newItvs.append(temp)
                    temp = Interval(left, d[left])

        if temp != None:
            newItvs.append(temp)

        return itvs1 + newItvs + itvs2