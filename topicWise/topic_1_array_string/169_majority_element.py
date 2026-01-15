from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, ele = 1, nums[0]

        for n in nums[1:]:
            if n != ele:
                if count == 0:
                    ele = n
                    count = 1
                    continue
                count -= 1
            else:
                count += 1
        
        return ele