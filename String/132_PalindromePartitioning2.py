class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        n = len(s)
        pal = [[False for i in range(n)] for j in range(n)]
        min_cut = [i for i in range(n)]
        for i in range(n):
            m = i
            for j in range(i+1):
                if s[i]==s[j] and i>j:
                    pal[i][j] = True
                    m = 0 if j==0 else min(m, min_cut[j-1])
            min_cut[i] = m
        return min_cut[n-1]
