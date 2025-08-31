class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        perimeter = 0
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            nonlocal perimeter
            if (
                r not in range(ROWS)
                or c not in range(COLS)
                or (r, c) in visited
                or grid[r][c] == 0
            ):
                return

            visited.add((r, c))

            for dr, dc in directions:
                if (
                    r + dr not in range(ROWS)
                    or c + dc not in range(COLS)
                    or grid[r + dr][c + dc] == 0
                ):
                    perimeter += 1
                dfs(r + dr, c + dc)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    dfs(row, col)
                    break

        return perimeter
