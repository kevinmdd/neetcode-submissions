class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i = 0
        j = 0
        check = [set() for _ in range(9)]
        column_check = [set() for _ in range(9)]
        # s = {key: [] for key in range(1, 10)}
        # 1 : [], 
        key_increment = 0 
        new_box = 0
        valid = True
        for i in range(len(board)):
            if (i % 3) == 0 and i > 0:
                new_box = i
            key_increment = new_box
            row_check = set()
            for j in range(len(board)):
                if (j % 3) == 0 and j > 0:
                    key_increment += 1
                if board[i][j] in check[key_increment] and board[i][j] != '.':
                    print(f"invalid 3x3 value: {board[i][j]}")
                    valid = False
                    break
                if board[i][j] in row_check and board[i][j] != '.':
                    print(f"invalid row value: {board[i][j]}")
                    valid = False
                    break
                if board[i][j] in column_check[j] and board[i][j] != '.':
                    print(f"invalid column value: {board[i][j]}")
                    valid = False 
                    break
                if board[i][j] != '.':
                    # if j == 3:
                        #  print(f"column set: {column_check}, to_add: {board[i][j]}, index: {j}")
                    # print(f'key: {key_increment}, i index: {i}, j index: {j}, to add: {board[i][j]}')
                    # print(f"row set: {row_check}, to_add: {board[i][j]}")
                    check[key_increment].add(board[i][j])
                    row_check.add(board[i][j])
                    column_check[j].add(board[i][j])
        
        print(column_check)
        print(check)
        return valid
                

