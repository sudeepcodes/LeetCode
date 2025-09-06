from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        DIRECTORY = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        result = []

        def backtrack(i, path):
            if i >= len(digits):
                if path:
                    result.append(path)
                return
            
            for ch in DIRECTORY[digits[i]]:
                path += ch
                backtrack(i+1, path)
                path = path[:-1]
        
        backtrack(0, '')
        return result