from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        cur_sum, max_sum = 0, 0
        cur_dict = {}

        while j < len(nums):
            if (j - i) == k:
                if len(cur_dict) == k:
                    max_sum = max(max_sum, cur_sum)

                if cur_dict[nums[i]] == 1:
                    del (cur_dict[nums[i]])
                else:
                    cur_dict[nums[i]] -= 1
                cur_sum -= nums[i]
                i += 1
            else:
                cur_sum += nums[j]
                cur_dict[nums[j]] = 1 + cur_dict.get(nums[j], 0)
                j += 1

        if len(cur_dict) == k:
            max_sum = max(max_sum, cur_sum)
        return max_sum


# print(Solution().maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3))
print(Solution().maximumSubarraySum([1, 1, 1, 7, 8, 9], 3))
