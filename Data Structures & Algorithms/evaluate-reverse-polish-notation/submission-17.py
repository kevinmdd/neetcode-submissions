class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        s = []
        operands = {"+": lambda x, y: x + y, "*": lambda x, y: x * y, 
        "-": lambda x, y: x - y, "/": lambda x, y: x / y}
        i = 0
        for token in tokens:
            if token not in "+*-/":
                s.append(int(token))
                continue
            if s:
                if len(s) > 1: 
                    s1, s2 = s.pop(), s.pop()
                    s.append(int(operands.get(token)(s2, s1)))
        return int(s.pop())
