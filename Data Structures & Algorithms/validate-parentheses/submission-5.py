class Solution:
    def isValid(self, s: str) -> bool:
        parenthese = { ")" : "(", "]" : "[", "}" : "{" }
        stack = []

        for c in s:
            if c in parenthese:
                if stack and stack[-1] == parenthese[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
    
        return True if not stack else False