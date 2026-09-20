class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+': lambda a, b: int(a + b),'-': lambda a, b: int(a - b),'*': lambda a, b: int(a * b),'/': lambda a, b: int(a / b)}        
        numbers = []

        for token in tokens:
            if token not in operators :
                numbers.append(int(token))
            else:
                if len(numbers) >= 2:
                    a = numbers.pop()
                    b = numbers.pop()
                    numbers.append(operators[token](b, a))
        return numbers.pop()
