from typing import List


class Solution:
    def is_ones(self, matrix, tl, br):
        dims = br[0] - tl[0] + 1
        sr, sc = tl
        for r in range(dims):
            for c in range(dims):
                if matrix[sr + r][sc + c] != 1:
                    return False
        return True

    def countSquares(self, matrix: List[List[int]]) -> int:
        pass


mat = [
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]
print(Solution().is_ones(mat, (0, 1), (2, 3)))
