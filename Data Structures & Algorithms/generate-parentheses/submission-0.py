class Solution:   
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(current, closeCount, openCount):
            if openCount == n and closeCount == n:
                result.append(current)

            if openCount < n:
                backtrack(current + '(', closeCount, openCount+1)
            if closeCount < min(openCount,n):    
                backtrack(current + ')', closeCount+1, openCount)
        

        backtrack("",0,0)
        return result
