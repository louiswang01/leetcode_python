"""
2 loops
1. store locations of 0 using the first row and first column
2. modify the matrix
"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows=len(matrix)
        cols=len(matrix[0])
        row_transfer=set()
        row_zero=[0 for i in range(cols)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    row_transfer.add(j)
        
        for i in range(rows):
            if matrix[i][0]==0:
                matrix[i]=row_zero
            else:
                matrix[i]=[0 if k in row_transfer else matrix[i][k] for k in range(cols)]
