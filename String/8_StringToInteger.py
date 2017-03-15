# This solution is inefficient.. Need a second try

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        flag = False

        intstr = ""

        if str == "":
            return 0

        for c in str:
            if flag == False:
                if c.isdigit() == True:
                    flag = True
                    intstr += c
                else:
                    if c == "+":
                        flag = True
                    elif c == "-":
                        flag = True
                        intstr += "-"
                    elif c == " ":
                        continue
                    else:
                        break
            else:
                if c.isdigit() == True:
                    intstr += c
                    if len(intstr) > 11:
                        break
                else:
                    break

        if flag == False:
            return 0

        if len(intstr) == 0 or intstr == "-":
            return 0

        int1 = int(intstr)

        # overflow
        if int1 > 2147483647:
            return 2147483647
        elif int1 < -2147483648:
            return -2147483648

        return int(intstr)



