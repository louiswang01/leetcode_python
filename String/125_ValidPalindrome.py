class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "" or len(s) == 1:
            return True

        i = 0
        j = len(s) - 1
        s = s.lower()

        while i <= j:
            if i == j:
                return True
            if s[i].isalnum() == True:
                if s[j].isalnum() == True:
                    if s[i] == s[j]:
                        i += 1
                        j -= 1
                    else:
                        return False
                else:
                    j -= 1
            else:
                i += 1

        return True