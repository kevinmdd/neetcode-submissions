class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens.pop())
        s = []
        operands = {"+": lambda x, y: x + y, "*": lambda x, y: x * y, 
        "-": lambda x, y: x - y, "/": lambda x, y: x / y}
        for token in tokens:
            if token not in "+*-/":
                s.append(int(token))
                continue
            if s:
                if len(s) > 1: 
                    s1, s2 = s.pop(), s.pop()
                    s.append(int(operands.get(token)(s2, s1)))
                    continue
            s.append(int(token))
        return int(s.pop())
