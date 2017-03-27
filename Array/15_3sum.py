"""
1. loop through 0 to n-2
2. 2 pointers move towards each other from the end of two sides of array
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = []
        nums.sort()

        for i in range(len(nums) - 2):
            n1 = i + 1
            n2 = len(nums) - 1

            if i > 0:
                if nums[i] == nums[i - 1]:
                    continue

            target = 0 - nums[i]

            while n1 < n2:
                if nums[n1] + nums[n2] < target:
                    n1 += 1
                elif nums[n1] + nums[n2] > target:
                    n2 -= 1
                else:
                    l.append([nums[i], nums[n1], nums[n2]])
                    n1 += 1
                    n2 -= 1
                    while (nums[n1] == nums[n1 - 1] and nums[n2] == nums[n2 + 1]) and n2 > n1:
                        n1 += 1

        return l
