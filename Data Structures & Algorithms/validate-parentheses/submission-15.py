class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 1:
            return False
        for char in s:
            if char in "({[":
                stack.append(char)
            elif char in ")}]":
                if len(stack) != 0:
                    if (stack[len(stack)-1] + char)  == "()" or  (stack[len(stack)-1] + char) == "[]" or (stack[len(stack)-1] + char)  == "{}":
                        stack.remove(stack[len(stack)-1])
                    else:
                        return False
                else:
                    return False

        if len(stack) != 0:
            return False
        return True