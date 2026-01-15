from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        def check_valid(row, col):
            # check the row
            for r in range(ROWS):
                if r != row and board[row][col] == board[r][col]:
                    return False
            
            # check the col
            for c in range(COLS):
                if c != col and board[row][col] == board[row][c]:
                    return False
                
            # check sub grid
            sr = row - row % 3
            sc = col - col % 3
            for r in range(sr, sr+3):
                for c in range(sc, sc+3):
                    if (r, c) != (row, col) and board[r][c] == board[row][col]:
                        return False
            
            return True
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] != '.' and not check_valid(r, c):
                    return False
        
        return True

