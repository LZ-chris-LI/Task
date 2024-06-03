
#Task 1
def reverse_list(l:list):

    """

    TODO: Reverse a list without using any built in functions

 

    The function should return a sorted list.

    Input l is a list which can contain any type of data.

    """

    #using two-pointer to solve it
    start = 0
    end = len(l)-1
    while (start < end):
        l[start],l[end] = l[end], l[start]
        start += 1
        end -= 1
    return l

# l = []
# print(reverse_list(l))


#Task2
def solve_sudoku(matrix):

    """

    TODO: Write a programme to solve 9x9 Sudoku board.

 

    Sudoku is one of the most popular puzzle games of all time. The goal of Sudoku is to fill a 9×9 grid with numbers so that each row, column and 3×3 section contain all of the digits between 1 and 9. As a logic puzzle, Sudoku is also an excellent brain game.

 

    The input matrix is a 9x9 matrix. You need to write a program to solve it.

    """

    #helper function to check is the number in the row, column or box
    def isValid(num, row, col):
        for i in range(9):
            if matrix[row][i] == num or matrix[i][col] == num or matrix[3*(row//3)+i//3][3*(col//3)+i%3] == num:
                return False
        return True
    
    #use backtrack to fill the empty cell
    def solve(row,col):
        
        if col == 9:                #the col and row count from 0 to 8. Detecting if the col of num out of bound, go to the next row or return True if the num in the last row already
            if row == 8:
                return True
            row += 1
            col = 0
        
        if matrix[row][col] > 0:
            return solve(row,col+1)     #because we figured out moving to the next line above, therefore we don't need to do anything on row
        
        for num in range(1,10):
            if isValid(num, row, col):
                matrix[row][col] = num

                if solve(row,col+1):
                    return True
            matrix[row][col] = 0
        return False
    
    if solve(0,0):
        return True
    else:
        return False


#Output test

# matrix = [[6, 5, 0, 0, 3, 0, 9, 0, 1],
#     [0, 1, 0, 0, 0, 4, 0, 0, 0],
# 	[4, 0, 7, 0, 0, 0, 2, 0, 8],
# 	[0, 0, 5, 2, 0, 0, 0, 0, 0],
# 	[0, 0, 0, 0, 9, 8, 1, 0, 0],
# 	[0, 4, 0, 0, 0, 3, 0, 0, 0],
# 	[0, 0, 0, 3, 6, 0, 0, 7, 2],
# 	[0, 7, 0, 0, 0, 0, 0, 0, 3],
# 	[9, 0, 3, 0, 0, 0, 6, 0, 4]]


# if solve_sudoku(matrix):
#     print(matrix)
# else:
#     print("NO solution")

