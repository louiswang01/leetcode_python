# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []

        # construct interval dictionary
        d = {}
        for itv in intervals:
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

        return newItvs
