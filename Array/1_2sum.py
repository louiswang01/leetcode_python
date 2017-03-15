class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}

        for i in range(len(nums)):
            if not nums[i] in d:
                d[nums[i]] = i

        l = []
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in d and \
                            d[temp] != i:
                l.append(i)
                l.append(d[temp])
                break

        return l