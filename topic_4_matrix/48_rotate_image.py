from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # Transpose the matrix 
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reverse the rows
        for r in range(n):
            i, j = 0, n-1
            while i < j:
                matrix[r][i], matrix[r][j] = matrix[r][j], matrix[r][i]
                i += 1
                j -= 1