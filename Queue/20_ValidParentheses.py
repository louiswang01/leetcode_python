class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        flag = True

        if len(s) == 0:
            return False

        for c in s:
            if c == "{" or c == "(" or c == "[":
                stack.append(c)
            elif c == "}" or c == ")" or c == "]":
                if len(stack) == 0:
                    return False
                else:
                    cc = stack.pop()
                    if (c == "}" and cc != "{") or \
                            (c == ")" and cc != "(") or \
                            (c == "]" and cc != "["):
                        return False
        if len(stack) > 0:
            return False
        else:
            return True
