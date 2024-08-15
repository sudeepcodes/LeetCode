import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        heap = []
        ans = 0
        visited = set()

        heapq.heappush(heap, (matrix[0][0], 0, 0))
        visited.add((0, 0))

        while k and heap:
            ans, i, j = heapq.heappop(heap)

            if i + 1 < ROWS and (i + 1, j) not in visited:
                heapq.heappush(heap, (matrix[i + 1][j], i + 1, j))
                visited.add((i + 1, j))

            if j + 1 < COLS and (i, j + 1) not in visited:
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
                visited.add((i, j + 1))

            k -= 1

        return ans

# TC: O(k . log k)  - k elements + log k for pushing & popping k elements in heap
# SC: O(k) for heap + O(ROWS * COLS) for visited set = O(k + n^2)
