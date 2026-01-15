'''
Given integers n and target, construct a sequence of length n such that:

    The absolute values are a permutation of {1..n}.
    The sum of the sequence equals target.

Among all valid sequences, return the lexicographically smallest.

Input: n=4, target=-2

Valid sequences:
[-1, -2, -3, 4]
[ 3, -2, 1, -4]
[-4, -2, 1, 3] <-- lexicographically smallest

Output: [-4, -2, 1, 3]
'''
from typing import List


class Solution:
    def constructSequenceBruteForce(self, n: int, target: int) -> List[int]:
        valid_sequences = set()

        def dfs(i, path):
            if i >= (n+1):
                if sum(path) == target:
                    valid_sequences.add(tuple(sorted(path)))
                return
            path.append(i)
            dfs(i + 1, path)
            path.pop()

            path.append(-i)
            dfs(i + 1, path)
            path.pop()
        
        dfs(1, [])
        return list(valid_sequences)[0]

    def constructSequenceOptimal(self, n: int, target: int) -> List[int]:
        nums = [-i for i in range(n, 0,-1)]
        ans = []

        def dfs(i, cur_sum, path):
            nonlocal ans
            if ans:
                return
            
            if i == len(nums):
                if cur_sum == target:
                    ans = path[:]
                return
            
            path.append(nums[i])
            dfs(i+1, cur_sum + nums[i], path)
            path.pop()

            path.append(-nums[i])
            dfs(i+1, cur_sum - nums[i], path)
            path.pop()
        
        dfs(0, 0, [])
        return ans


print(Solution().constructSequenceOptimal(4, -2))
