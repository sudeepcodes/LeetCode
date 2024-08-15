from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(i, seq):
            nonlocal ans
            if i >= len(candidates) or sum(seq) > target:
                return

            if sum(seq) == target:
                ans.append(seq[:])
                return

            seq.append(candidates[i])
            dfs(i, seq)

            seq.pop()
            dfs(i + 1, seq)

        dfs(0, [])
        return ans

# TC: O(2^n)
# SC: O(n) for recursive stack i.e. the max depth of recursion

