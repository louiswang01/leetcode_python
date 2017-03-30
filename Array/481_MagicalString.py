"""
Method 1:
Its time complexity is O(n) and its space complexity is O(logn) by using generator. The drawback is its relatively low speed.

There exists two generator instance, one for the original sequence and the other one for generating next value in the original sequence. And this method use enumerator to calculate the next value to be 1 or 2. 


Method 2:
Its time complexity and space complexity are both O(n). Its advantage is its high speed.

Method 3:
An improved version of method 2. Use 0 instead of 2 to make the sum of the sequence equal to the number of ones.
"""


from itertools import islice
class Solution(object):
    # Method 1
    def magicalString1(self, n):
        """
        :type n: int
        :rtype: int
        """
        def gen():
            for i in 1,2,2:
                yield i
            for i, x in enumerate(gen()):
                if i >=2:
                    for j in range(x):
                        yield i%2+1
        return sum(x & 1 for x in islice(gen(),n))

    # Method 2
    def magicalString2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        elif n<4:
            return 1
        seq=[1,2,2]
        pointer=2
        ones=1
        while len(seq)<n:
            new_val=3-seq[-1]
            seq.append(new_val)
            if seq[pointer]==1:
                if new_val==1:
                    ones+=1
            elif len(seq)<n:
                seq.append(new_val)
                if new_val==1:
                    ones+=2
            else:
                if new_val==1:
                    ones+=1
                break
            pointer+=1
        return ones

    # Method 3
    def magicalString3(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        elif n<4:
            return 1
        seq=[1,0,0]
        pointer=2
        while len(seq)<n:
            new_val=1-seq[-1]
            seq.append(new_val)
            if seq[pointer]==0:
                if len(seq)<n:
                    seq.append(new_val)
                else:
                    break
            pointer+=1
        return sum(seq)
