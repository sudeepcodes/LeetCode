from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums) - 1

        # swap out vals to the end of the list
        while i <= j:
            if nums[i] != val:
                i += 1
            else:
                nums[i] = nums[j]
                j -= 1
        
        return j + 1