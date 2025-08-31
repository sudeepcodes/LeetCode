from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_count = {
            5: 0,
            10: 0
        }

        for bill in bills:
            if bill == 5:
                bill_count[5] += 1
            elif bill == 10 and bill_count[5] >= 1:
                bill_count[10] += 1
                bill_count[5] -= 1
            elif bill == 20 and bill_count[10] >= 1 and bill_count[5] >= 1:
                bill_count[10] -= 1
                bill_count[5] -= 1
            elif bill == 20 and bill_count[5] >= 3:
                bill_count[5] -= 3
            else:
                return False
        return True

# TC: O(n)
# SC: O(1)
