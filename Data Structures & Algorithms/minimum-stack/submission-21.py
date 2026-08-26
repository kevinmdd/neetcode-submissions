class MinStack:
    def __init__(self):
        self.stack = []
        self.min_list = []

    def push(self, val: int) -> None:
        if not self.min_list:
            self.min_list.append(val)
        elif val <= self.min_list[-1]:
            self.min_list.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.min_list[-1]:
            self.min_list.pop()
        self.stack.pop()

    def top(self) -> int:   
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_list[-1]
        
