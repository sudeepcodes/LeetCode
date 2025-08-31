# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        top, bottom = 0, m
        left, right = 0, n

        while top < bottom and left < right:
            # top row
            for i in range(left, right):
                if head:
                    matrix[top][i] = head.val
                    head = head.next
                else:
                    break
            top += 1

            # right column
            for i in range(top, bottom):
                if head:
                    matrix[i][right-1] = head.val
                    head = head.next
                else:
                    break
            right -= 1

            if not (left < right and top < bottom):
                break

            # bottom row reversed
            for i in range(right-1, left -1, -1):
                if head:
                    matrix[bottom-1][i] = head.val
                    head = head.next
                else:
                    break
            bottom -= 1

            # left column reversed
            for i in range(bottom-1, top-1, -1):
                if head:
                    matrix[i][left] = head.val
                    head = head.next
                else:
                    break
            left += 1
        
        return matrix
