class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = [(position[i], speed[i]) for i in range(len(position))]
        combined = sorted(combined, key=lambda x: x[0], reverse=True)
        stack = []

        for i in range(len(position)):
            if not stack:
                stack.append((target - combined[i][0]) / combined[i][1])
            if stack[-1] < (target - combined[i][0]) / combined[i][1] :
                stack.append((target - combined[i][0]) / combined[i][1])

        return len(stack)
