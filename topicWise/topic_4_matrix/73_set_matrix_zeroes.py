from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = [], []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    ROWS.append(i)
                    COLS.append(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in ROWS or j in COLS:
                    matrix[i][j] = 0
