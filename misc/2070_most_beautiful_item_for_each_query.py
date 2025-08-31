from typing import List


class Solution:
    def search(self, l, r, arr, target):
        res = -1
        while l <= r:
            m = (l + r) // 2
            if arr[m][0] == target:
                res = m
                l = m + 1
            elif arr[m][0] > target:
                r = m - 1
            else:
                res = m
                l = m + 1
        return res

    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        for i in range(len(queries)):
            item_index = self.search(0, len(items)-1, items, queries[i])
            if item_index == -1:
                queries[i] = 0
            else:
                queries[i] = items[item_index][1]

        return queries

print(Solution().maximumBeauty(
    items=[[1, 2], [2, 4], [3, 2], [3, 5], [5, 6]],
    queries=[1, 2, 3, 4, 5, 6]
))

print(Solution().maximumBeauty(
    items=[[10,1000]],
    queries=[5]
))

