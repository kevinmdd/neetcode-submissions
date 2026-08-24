class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 1:
            return False
        for char in s:
            if char in "({[":
                stack.append(char)
            elif char in ")}]":
                if len(stack) == 0:
                    return False
                check = stack[-1] + char
                if check == "()" or check == "[]" or check == "{}":
                    stack.remove(stack[-1])
                else:
                    return False
        if len(stack) != 0:
            return False
        return True