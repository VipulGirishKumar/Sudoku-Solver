import time

board = [[4, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 9, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 7, 8, 5],
         [0, 0, 7, 0, 4, 8, 0, 5, 0],
         [0, 0, 1, 3, 0, 0, 0, 0, 0],
         [0, 0, 6, 0, 7, 0, 0, 0, 0],
         [8, 6, 0, 0, 0, 0, 9, 0, 3],
         [7, 0, 0, 0, 0, 5, 0, 6, 2],
         [0, 0, 3, 7, 0, 0, 0, 0, 0]]


def printSudokuBoard(board):
    for row in range(0, len(board)):
        for column in range(0, len(board[row])):
            print(board[row][column], end = '')
        print()


def searchForEmptyGrid(board):
    for row in range(0, len(board)):
        for column in range(0, len(board[row])):
            if board[row][column] == 0:
                return (row, column)
    else:
        return None


def checkRow(board, number, row, column):
    for i in range(0, len(board)):
        if i != column and board[row][i] == number:
            return False
    else:
        return True

def checkColumn(board, number, row, column):
    for i in range(0, len(board)):
        if i != column and board[i][column] == number:
            return False
    else:
        return True

def getBlock(board, row, column):
    blockRow = (row//3)*3
    blockColumn = (column//3)*3
    blockNumbers = []

    for i in range(3):
        for j in range(3):
            blockNumbers.append(board[blockRow+i][blockColumn+j])
    return blockNumbers


def checkBlock(getblock, number):
    for i in range(0, len(getblock)):
        if getblock[i] == number:
            return False
    else:
        return True


def solveBoard(board):
    
    gridCoord = searchForEmptyGrid(board)
    
    if gridCoord:
        row, column = gridCoord[0],gridCoord[1]
    else:
        printSudokuBoard(board)
        return True
    

    for i in range(1, 10):
        if checkBlock(getBlock(board, row, column), i) and \
                checkRow(board, i, row, column) and \
                checkColumn(board, i, row, column):
            board[row][column] = i

            if solveBoard(board):
                return board

            else:
                board[row][column] = 0

    return False

start_time = time.time()
solveBoard(board)
print(time.time() - start_time)

