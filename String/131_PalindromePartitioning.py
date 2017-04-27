class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if s=='':
            return [[]]
        if len(s) == 1:
            return [[s]]
        
        isPalindrome = lambda x: x == x[::-1] # efficient check

        result=[]
        for i in range(len(s)):
            if isPalindrome(s[:i+1]):
                re = self.partition(s[i+1:])
                for r in re:
                    result.append([s[:i+1]]+r)
        return result

    """
    # This function could be replaced by lambda function
    def isPalindrome(self, s1):
        q=[]
        num=len(s1)
        for i in range(num/2):
            if s1[i]!=s1[-i-1]:
                return False
        return True
    """

