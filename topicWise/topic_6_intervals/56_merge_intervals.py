from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort so that the starting times are in ascending order
        intervals.sort()

        merged = []
        # for each interval, check if it overlaps with the last in the result array
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # if overlap, update the ending time
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
