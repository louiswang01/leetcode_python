# This solution is inefficient.. Need a second try

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if needle == "":
            return 0

        j = 0
        p = -1
        flag = False

        i = 0
        while i < len(haystack):
            c = haystack[i]
            if flag == False:
                if c == needle[0]:
                    p = i
                    flag = True
                    j += 1
                i += 1
            else:
                if c == needle[j]:
                    j += 1
                    i += 1
                else:
                    j = 0
                    flag = False
                    i = p + 1
                    p = -1

            if j == len(needle):
                break

        if j != len(needle):
            return -1

        return p

