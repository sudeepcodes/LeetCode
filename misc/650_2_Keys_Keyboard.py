class Solution:
    def highest_factor(self, x):
        if x == 1:
            return 1

        for i in range(x // 2, 0, -1):
            if x % i == 0:
                return i

    def minSteps(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 0

        for i in range(2, n + 1):
            hf = self.highest_factor(i)
            q = i // hf
            dp[i] = dp[hf] + q

        return dp[n]
