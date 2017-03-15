class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        q = ["("]
        discovered = set()

        while q != []:
            vertex = q[-1]  # last element in list
            left = vertex.count("(")
            right = vertex.count(")")
            while left > right or left < n:
                if left + 1 <= n and vertex + "(" not in discovered:
                    left += 1
                    vertex += "("
                    q.append(vertex)
                    discovered.add(vertex)
                    continue
                elif right + 1 <= left and vertex + ")" not in discovered:
                    right += 1
                    vertex += ")"
                    q.append(vertex)
                    discovered.add(vertex)
                else:
                    break
            if len(vertex) == n * 2:
                result.append(vertex)
            q.pop()

        return result

