from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        _min, _max = arrays[0][0], arrays[0][-1]
        res = 0

        for subarr in arrays[1:]:
            res = max(
                res,
                max(
                    subarr[-1] - _min,
                    _max - subarr[0]
                )
            )
            _min = min(_min, subarr[0])
            _max = max(_max, subarr[-1])

        return res
