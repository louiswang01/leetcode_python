class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if s.isdigit() == True:
            return True

        if s == "":
            return False

        prefix = False
        digit = False
        dot = False
        expo = False
        cLast = ""

        for c in s:
            if c.isdigit() == True:
                digit = True
                if prefix == False:
                    prefix = True
            elif c == " ":
                return False
            elif c == "+" or c == "-":
                if prefix == False:
                    prefix = True
                else:
                    return False
            elif c == ".":
                if dot == False and expo == False:
                    prefix = True
                    dot = True
                else:
                    return False
            elif c == "e":
                if expo == True or digit == False:
                    return False
                elif cLast.isdigit() == False and cLast != ".":
                    return False
                else:
                    expo = True
                    prefix = False
            else:
                return False

            cLast = c

        if digit == False:
            return False

        if cLast == "e" or cLast == "+" or cLast == "-":
            return False

        return True

