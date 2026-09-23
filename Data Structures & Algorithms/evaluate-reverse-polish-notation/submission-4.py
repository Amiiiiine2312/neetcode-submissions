class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def add(x: int, y: int) -> int:
            return x + y

        def substract(x, y):
            return x - y

        def multiply(x, y):
            return x * y

        def divide(x, y):
            return int(x / y)

        operator = {"+": add, "-": substract, "*": multiply, "/": divide}

        for i in range(len(tokens)):
            if tokens[i] not in operator:
                stack.append(int(tokens[i]))
            else:
                r = stack.pop()
                l = stack.pop()
                stack.append(operator[tokens[i]](l, r))
        return stack[-1]
