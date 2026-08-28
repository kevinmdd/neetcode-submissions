class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        s = []
        operands = {"+": lambda x, y: x + y, "*": lambda x, y: x * y, 
        "-": lambda x, y: x - y, "/": lambda x, y: x / y}
        i = 0
        while i < len(tokens):
            if tokens[i] not in "+*-/":
                s.append(int(tokens[i]))
                i += 1
            if tokens[i] in "+*-/":
                if s:
                    if len(s) > 1: 
                        s1, s2 = s.pop(), s.pop()
                        s.append(int(operands.get(tokens[i])(s2, s1)))
                i += 1
        return int(s.pop())
