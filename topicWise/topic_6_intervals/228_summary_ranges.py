from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums

        s, e = 0, 0
        ranges = []
        while e < len(nums) - 1:
            if nums[e+1] == nums[e] + 1:
                e += 1
            else:
                if s == e:
                    ranges.append(str(nums[s]))
                else:
                    ranges.append(f'{nums[s]}->{nums[e]}')
                e += 1
                s = e
        
        if s == e:
            ranges.append(str(nums[s]))
        else:
            ranges.append(f'{nums[s]}->{nums[e]}')
        return ranges