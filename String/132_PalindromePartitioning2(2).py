class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]: return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        dp=[0]*(len(s)+1)
        for i in range(1,len(dp)):
            if s[:i]!=s[0:i][::-1]:
                dp[i]=min(dp[j] for j in range(i) if s[j:i]==s[j:i][::-1])+1
        return dp[-1]     
