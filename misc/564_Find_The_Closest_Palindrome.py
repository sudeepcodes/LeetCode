class Solution:
    def nearestPalindromic(self, n: str) -> str:
        size = len(n)
        candidates = []

        prefix = n[:size // 2]
        if size % 2 == 0:
            candidates.append(prefix + prefix[::-1])
        else:
            candidates.append(prefix + n[size // 2] + prefix[::-1])

        prefix = str(int(prefix) + 1)
        if size % 2 == 0:
            candidates.append(prefix + prefix[::-1])
        else:
            candidates.append(prefix + n[size // 2] + prefix[::-1])

        prefix = str(int(prefix) - 2)
        if size % 2 == 0:
            candidates.append(prefix + prefix[::-1])
        else:
            candidates.append(prefix + n[size // 2] + prefix[::-1])

        candidates.append('9' * (size-1))
        candidates.append('1' + '0' * (size-1) + '1')

        candidates = [int(candidate) for candidate in candidates]
        print(candidates)
        diff = {}
        min_diff = 10**18 + 1

        for candidate in candidates:
            abs_diff = abs(int(n) - candidate)
            if abs_diff == 0:
                continue

            if abs_diff in diff:
                diff[abs_diff] = min(diff[abs_diff], candidate)
            else:
                diff[abs_diff] = candidate
            min_diff = min(abs_diff, min_diff)

        return diff[min_diff]


print(Solution().nearestPalindromic('807045053224792883'))