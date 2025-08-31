class Solution:
    def nthUglyNumber(self, n: int) -> int:
        result = [1]

        p1, p2, p3 = 0, 0, 0

        for i in range(n):
            m2 = result[p1] * 2
            m3 = result[p2] * 3
            m5 = result[p3] * 5

            result.append(min(m2, min(m3, m5)))

            if result[-1] == m2:
                p1 += 1
            if result[-1] == m3:
                p2 += 1
            if result[-1] == m5:
                p3 += 1

        return result[n - 1]
