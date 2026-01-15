from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = [(0,1), (0,-1), (1,0), (-1,0), (-1,-1), (-1,1), (1,-1), (1,1)]
        changed_states = {}

        for r in range(ROWS):
            for c in range(COLS):
                n1 = 0
                for dr, dc in DIRECTIONS:
                    if 0 <= r + dr < ROWS and 0 <= c+dc < COLS:
                        if board[r+dr][c+dc] == 1:
                            n1 += 1
                # if is live
                if board[r][c] == 1:
                    if n1 < 2:
                        changed_states[(r, c)] = 0
                    elif n1 > 3:
                        changed_states[(r, c)] = 0
                else:
                    if n1 == 3:
                        changed_states[(r, c)] = 1

        for (r,c), v in changed_states.items():
            board[r][c] = v


        