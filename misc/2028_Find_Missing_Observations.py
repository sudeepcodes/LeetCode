from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total_rolls = len(rolls) + n
        total_sum = mean * total_rolls
        sum_of_rolls = sum(rolls)
        sum_missing = total_sum - sum_of_rolls

        if n <= sum_missing <= 6 * n:
            result = [1] * n
            sum_remaining = sum_missing - n

            for i in range(len(result)):
                add = min(5, sum_remaining)
                result[i] += add
                sum_remaining -= add

            return result
        else:
            return []


print(Solution().missingRolls([3, 2, 4, 3], 4, 2))
