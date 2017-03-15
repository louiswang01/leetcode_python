class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 1

        two_step_to_end = 1
        one_step_to_end = 1

        for i in range(2, n):
            temp = one_step_to_end
            one_step_to_end = two_step_to_end + one_step_to_end
            two_step_to_end = temp

        return two_step_to_end + one_step_to_end