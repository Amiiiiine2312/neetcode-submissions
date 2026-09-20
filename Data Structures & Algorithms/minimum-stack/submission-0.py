class MinStack:

    def __init__(self):
        self.ministack = []

    def push(self, val: int) -> None:
        if self.ministack == []:
            self.ministack.append((val, val))
        else:
            self.ministack.append((val,min(val, self.ministack[-1][1])))

    def pop(self) -> None:
        self.ministack.pop()

    def top(self) -> int:
        return self.ministack[-1][0]

    def getMin(self) -> int:
        return self.ministack[-1][1]
        
