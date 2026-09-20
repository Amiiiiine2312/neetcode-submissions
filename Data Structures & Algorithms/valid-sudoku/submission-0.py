class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dictLignes = defaultdict(list)
        dictCol = defaultdict(list)
        dictCar = defaultdict(list)

        for i in range (9):
            for j in range (9):
                if board[i][j] != "." :
                    if board[i][j] in dictLignes[i] :
                        return False
                    else:
                        dictLignes[i].append(board[i][j])

                    if board[i][j] in dictCol[j] :
                        return False
                    else:
                        dictCol[j].append(board[i][j])

                    if board[i][j] in dictCar[(i//3, j//3)]:
                        return False
                    else:
                        dictCar[(i//3, j//3)].append(board[i][j])
                else :
                    continue
        return True
