from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val, max_len, cur = 0, 0, 0

        for n in nums:
            if max_val < n:
                max_val = n
                max_len = 0
                cur = 0

            if max_val == n:
                cur += 1
            else:
                cur = 0

            max_len = max(max_len, cur)

        return max_len

