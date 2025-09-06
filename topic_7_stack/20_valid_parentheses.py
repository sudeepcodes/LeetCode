class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for br in s:
            if br not in brackets:
                stack.append(br)
            else:
                if stack and stack[-1] == brackets[br]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
