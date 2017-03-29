"""
1. Use dictionary as it requires O(n) complexity
2. Key is number and value is boolean to record whether the key has been visited
3. Loop through the dictionary and look for consecutive elements on both sides of the element
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict={n:False for n in nums}
        max_len=0
        for num in dict:
            if dict[num]==False:
                dict[num]=True
                temp_len=1
                new_num=num
                while True:
                    new_num+=1
                    if new_num in dict:
                        dict[new_num]=True
                        temp_len+=1
                    else:
                        break
                new_num=num
                while True:
                    new_num-=1
                    if new_num in dict:
                        dict[new_num]=True
                        temp_len+=1
                    else:
                        break
                max_len=max(temp_len,max_len)
        return max_len
