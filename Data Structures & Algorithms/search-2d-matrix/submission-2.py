class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        # Find the correct row
        row_start, row_end = 0, len(matrix) - 1
        row = -1
        while row_start <= row_end:
            mid = (row_start + row_end) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif target < matrix[mid][0]:
                row_end = mid - 1
            else:
                row_start = mid + 1
        
        if row == -1:  # target not in any row
            return False
        
        # Binary search in the row
        col_start, col_end = 0, len(matrix[0]) - 1
        while col_start <= col_end:
            mid = (col_start + col_end) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                col_start = mid + 1
            else:
                col_end = mid - 1
        
        return False
