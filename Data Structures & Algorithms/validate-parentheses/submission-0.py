class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for i in s:
            if i in pair:
                if not stack or stack[-1] != pair[i]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)

        return not stack