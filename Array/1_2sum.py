class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
            
        nums_dict={}

        for i in range(len(nums)):
            need=target-nums[i]
            if need in nums_dict:
                return [nums_dict[need],i]
            nums_dict[nums[i]]=i