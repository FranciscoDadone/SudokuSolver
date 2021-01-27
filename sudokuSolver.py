
sudoku = [
     
    [
         0 ,  3 ,  6 ,      0 ,  0 ,  0 ,       0 ,  7 ,  0 
    ],[
         0 ,  9 ,  0 ,      0 ,  6 ,  0 ,       0 ,  0 ,  0 
    ],[
         0 ,  8 ,  1 ,      3 ,  0 ,  7 ,       0 ,  0 ,  2 
    ],
    
    ##########################################################
    
    [
         0 ,  0 ,  0 ,      6 ,  5 ,  3 ,       0 ,  4 ,  0 
    ],[
         0 ,  4 ,  5 ,      0 ,  0 ,  0 ,       2 ,  0 ,  0 
    ],[
         8 ,  0 ,  3 ,      9 ,  4 ,  0 ,       0 ,  0 ,  5 
    ],
    
    ############################################################
    
    [
         4 ,  0 ,  0 ,      8 ,  0 ,  0 ,       5 ,  3 ,  0 
    ],[
         0 ,  0 ,  0 ,      0 ,  0 ,  5 ,       0 ,  0 ,  7
    ],[
         3,   0 ,  7 ,      0,   0 ,  6 ,       0,   0 ,  0
    ]
    
]


def printTable():
     print('## ---------------------------------- ##')
     for sector in range(len(sudoku)):
        for number in range(len(sudoku[sector])):
            print(sudoku[sector][number], end=' ')
            if(number == 2 or number == 5 or number == 8):
                print('', end='  ')
        if(sector == 2 or sector == 5 or sector == 8):
            print('')
        print('')
     print('## ---------------------------------- ##')
    

def checkRow(row, number):
    canPut = True
    for n in sudoku[row]:
        if n == number:
            canPut = False
    return canPut



def checkCol(col, number):
     canPut = True
     for row in sudoku:
          if row[col] == number:
               canPut = False
     return canPut
       
       
        
def checkSector(row, col, number):
     rowInGrid = 0
     colInGrid = 0
     canPut = True
     
     # Find the row in the grid
     if row == 0 or row == 1 or row == 2:
          colInGrid = 0
     elif row == 3 or row == 4 or row == 5:
          colInGrid = 1
     elif row == 6 or row == 7 or row == 8:
          colInGrid = 2
          
     if col == 0 or col == 1 or col == 2:
          rowInGrid = 0
     elif col == 3 or col == 4 or col == 5:
          rowInGrid = 1
     elif col == 6 or col == 7 or col == 8:
          rowInGrid = 2
     
     # Gets the initial and end positions of the sector of the table
     rowi = rowInGrid * 3
     rowf = (rowInGrid * 3) + 2
     
     coli = colInGrid * 3
     colf = (colInGrid * 3) + 2
          
     # loops in the sector to find if there is a number in there
     for i in range(rowi, rowf + 1):
          for j in range(coli, colf + 1):
               if number == sudoku[i][j]:
                    canPut = False
     return canPut


def checkPlace(row, col, number):
     if checkRow(row, number) and checkCol(col, number) and checkSector(col, row, number):
          return True
     return False


##################################################################################################


printTable() # Prints the table before the solve function actuates

def solve():
     for row in range(9):
          for col in range(9):
               if sudoku[row][col] == 0:
                    for n in range(1,10):
                         if checkPlace(row, col, n):
                              sudoku[row][col] = n
                              solve()
                              sudoku[row][col] = 0
                    return
     printTable()
solve()