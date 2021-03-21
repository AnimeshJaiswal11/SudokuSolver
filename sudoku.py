sudoku = [["5","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]]


def print_sudoku(sudoku):
    for i in range(len(sudoku)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - -')
        for j in range(len(sudoku)):
            if j % 3 == 0 and j != 0:
                print(' | ', end='')
            if j == 8:
                print(sudoku[i][j])
            else:
                print(sudoku[i][j] + ' ', end='')

def find_empty(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == '.':
                return (i,j)
    return None

def is_valid(num,pos,sudoku):
    #row_check
    for i in range(len(sudoku[0])):
        if sudoku[pos[0]][i] == num and pos[1] != i:
            return False
    #column_check
    for i in range(len(sudoku)):
        if sudoku[i][pos[1]] == num and i != pos[0]:
            return False
    #box_check
    box_x = pos[0]//3
    box_y = pos[1]//3
    for i in range(box_x*3 , box_x*3+3):
        for j in range(box_y*3 , box_y*3+3):
            if sudoku[i][j] == num and (i,j) != pos:
                return False
    return True

def solve(sudoku):
    find = find_empty(sudoku)
    if not find:
        return True
    else:
        row,col = find
    for i in range(1,10):
        if is_valid(str(i),(row,col),sudoku):
            sudoku[row][col] = str(i)
            if solve(sudoku):
                return True
            sudoku[row][col] = '.'
    return False

print_sudoku(sudoku)
solve(sudoku)
print('------------------------------')
print_sudoku(sudoku)

