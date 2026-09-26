import bisect

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i , j = 0,0
        while matrix[i][len(matrix[0])-1] < target and i<len(matrix)-1:
            i+=1

        if i == len(matrix):
            return False

        j = bisect.bisect_left(matrix[i], target)
        
        return True if j < len(matrix[0]) and matrix[i][j] == target else False