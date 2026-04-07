class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        closing_brackets = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        stack = []
        for c in s:
            if c in closing_brackets:
                if stack and stack[-1] == closing_brackets[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
