# Welcome to sudoku solver
# Enter your input in the sudoku given below
# Use 0 for blank spaces

import numpy

# Enter your input below here.
sudoku = [[0, 0, 6, 0, 7, 3, 0, 0, 9],
          [0, 0, 0, 8, 0, 0, 0, 0, 0],
          [5, 7, 0, 0, 0, 6, 0, 0, 0],
          [1, 0, 0, 0, 0, 0, 6, 0, 5],
          [8, 9, 0, 0, 0, 7, 1, 3, 0],
          [0, 0, 0, 0, 3, 1, 0, 8, 0],
          [0, 0, 0, 0, 0, 0, 7, 4, 0],
          [0, 4, 5, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 9, 3, 0, 8]]


def sudoku_checker(row, column, number):
    global sudoku
    for i in range(0, 9):
        if sudoku[row][i] == number:
            return False
    for i in range(0, 9):
        if sudoku[i][column] == number:
            return False
    xrow = (column // 3) * 3     #Checking for 3*3 boxes
    ycolumn = (row // 3) * 3     #Checking for 3*3 boxes
    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku[ycolumn + i][xrow + j] == number:
                return False
    return True


def sudoku_solver():
    global sudoku
    for row in range(0, 9):
        for column in range(0, 9):
            if sudoku[row][column] == 0:
                for number in range(1, 10):
                    if sudoku_checker(row, column, number):
                        sudoku[row][column] = number
                        sudoku_solver()
                        sudoku[row][column] = 0
                return


    print(numpy.matrix(sudoku))

print("Your solved sudoku is given below.\n")
sudoku_solver()
