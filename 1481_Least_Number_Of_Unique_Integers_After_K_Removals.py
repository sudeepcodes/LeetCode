from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = {}
        for a in arr:
            counts[a] = 1 + counts.get(a, 0)

        counts = sorted(counts.items(), key=lambda x: x[1])

        unique = 0
        for i in range(len(counts)):
            if k > 0:
                key, count = counts[i]
                if k >= count:
                    k -= count
                else:
                    unique += 1
            else:
                unique += 1

        return unique
