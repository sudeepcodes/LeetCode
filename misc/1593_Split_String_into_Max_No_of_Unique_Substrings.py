class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        subsets = set()

        i, j = 0, 0
        while j < len(s) - 1:
            cur = s[i:j + 1]
            if cur in subsets:
                j += 1
            else:
                subsets.add(s[i:j + 1])
                i = j + 1
                j += 1

        subsets.add(s[i:j+1])
        print(subsets)
        return len(subsets)

print(Solution().maxUniqueSplit('aba'))