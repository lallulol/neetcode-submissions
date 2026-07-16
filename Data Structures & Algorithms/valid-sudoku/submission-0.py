class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = [[] for _ in range(9)]
        for i in range(len(board)):
            row_list = []
            col_list = []
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    row_list.append(board[i][j])
                    box_index = (i//3)*3+(j//3)
                    boxes[box_index].append(board[i][j])
                if board[j][i] != ".":
                    col_list.append(board[j][i])
            if len(set(row_list)) != len(row_list):
                return False
            if len(set(col_list)) != len(col_list):
                return False
        for box in boxes:
            if len(set(box)) != len(box):
                return False
        return True
