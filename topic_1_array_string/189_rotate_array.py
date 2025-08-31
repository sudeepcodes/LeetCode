from typing import List


class Solution:
    def reverse(self, nums, i, j):
        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for cases where k > len(nums)
        k %= len(nums)

        pivot = len(nums) - k
        # reverse both sides of k, Kth element to be on right side
        self.reverse(nums=nums, i=0, j=pivot-1)
        self.reverse(nums=nums, i=pivot, j=len(nums)-1)

        # reverse the whole array
        self.reverse(nums=nums, i=0, j=len(nums)-1)