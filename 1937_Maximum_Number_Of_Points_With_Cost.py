from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ROWS, COLS = len(points), len(points[0])
        prev_row = points[0]

        for r in range(1, ROWS):
            left_max, right_max, current_row = [0] * COLS, [0] * COLS, [0] * COLS

            # left max
            left_max[0] = prev_row[0]
            for c in range(1, COLS):
                left_max[c] = max(prev_row[c], left_max[c - 1] - 1)

            # right max
            right_max[-1] = prev_row[-1]
            for c in range(COLS - 2, -1, -1):
                right_max[c] = max(prev_row[c], right_max[c + 1] - 1)

            # current_row
            for c in range(COLS):
                current_row[c] = points[r][c] + max(left_max[c], right_max[c])

            prev_row = current_row

        return max(prev_row)
