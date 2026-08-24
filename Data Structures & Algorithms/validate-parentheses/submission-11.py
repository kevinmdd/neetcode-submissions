class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_char = "({["
        closed_char = ")}]"
        if len(s) == 1:
            return False
        for char in s:
            if char in open_char:
                stack.append(char)
            elif char in closed_char:
                if len(stack) != 0:
                    check = "" + stack[len(stack)-1] + char
                    if check == "()" or check == "[]" or check == "{}":
                        stack.remove(stack[len(stack)-1])
                    else:
                        return False
                else:
                    return False

        if len(stack) != 0:
            return False
        return True