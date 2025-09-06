class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        stack = []

        for dir in dirs:
            if stack and dir == '..':
                stack.pop()
            elif dir not in ['..', '.', '']:
                stack.append(dir)
        return '/'+'/'.join(stack)

