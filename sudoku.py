# Test cases
def instantiateCases () :
    # Correctly Formulated Sudoku
    global s 
    s = [[0,0,7, 0,0,0, 0,1,5],
         [0,0,0, 3,9,7, 0,0,0],
         [0,6,2, 0,1,0, 4,0,9], 
         [0,2,0, 0,0,1, 5,4,3],
         [7,0,0, 4,0,9, 0,0,1],
         [4,8,1, 2,0,0, 0,6,0],
         [9,0,6, 0,2,0, 7,3,0],
         [0,0,0, 9,8,4, 0,0,0],
         [1,5,0, 0,0,0, 2,0,0]]    
    # Unsolvable Sudoku (Information Missing)
    global s2 
    s2 = [[0,0,0, 0,0,0, 0,1,5],
          [0,0,0, 3,9,7, 0,0,0],
          [0,0,0, 0,1,0, 4,0,9],
          [0,0,0, 0,0,1, 5,4,3],
          [0,0,0, 4,0,9, 0,0,1],
          [0,0,0, 2,0,0, 0,6,0],
          [0,0,0, 0,2,0, 7,3,0],
          [0,0,0, 9,8,4, 0,0,0],
          [0,0,0, 0,0,0, 2,0,0]]
    # Solved Sudoku
    global s3 
    s3 = [[8,9,7, 6,4,2, 3,1,5],
          [5,1,4, 3,9,7, 6,8,2],
          [3,6,2, 5,1,8, 4,7,9],
          [6,2,9, 8,7,1, 5,4,3],
          [7,3,5, 4,6,9, 8,2,1],
          [4,8,1, 2,5,3, 9,6,7],
          [9,4,6, 1,2,5, 7,3,8],
          [2,7,3, 9,8,4, 1,5,6],
          [1,5,8, 7,3,6, 2,9,4]]
    # Invalid Sudoku (Does not follow Rules of Sudoku)
    global s4 
    s4 = [[0,0,7, 0,0,0, 0,1,5],
          [0,0,0, 3,9,7, 0,0,0],
          [0,6,2, 0,1,0, 4,0,9], 
          [0,2,0, 0,0,1, 5,4,3],
          [7,0,0, 4,0,9, 0,0,1],
          [4,8,1, 2,0,0, 0,6,0],
          [9,0,6, 5,2,0, 7,3,0],
          [0,0,0, 9,8,4, 0,0,0],
          [1,3,6, 0,0,0, 2,0,0]]
    # s after one full application of elimination
    global s5 
    s5 = [[0,0,7, 0,0,0, 0,1,5],
          [0,0,0, 3,9,7, 0,0,0],
          [0,6,2, 0,1,0, 4,0,9],
          [6,2,9, 0,7,1, 5,4,3],
          [7,3,5, 4,6,9, 8,2,1],
          [4,8,1, 2,0,0, 9,6,7],
          [9,4,6, 0,2,5, 7,3,8],
          [0,7,3, 9,8,4, 0,5,6],
          [1,5,8, 0,3,6, 2,9,4]]
    # Medium Difficulty Sudoku, unsolvable by elimination method alone
    global m
    m = [[1,0,0, 9,0,8, 3,6,0],
         [0,0,5, 3,0,0, 4,0,0],
         [8,0,0, 6,5,0, 0,0,0],
         [0,0,0, 0,0,3, 0,9,2],
         [0,0,3, 0,0,0, 1,0,0],
         [5,6,0, 1,0,0, 0,0,0],
         [0,0,0, 0,7,6, 0,0,3],
         [0,0,6, 0,0,0, 2,0,0],
         [0,8,4, 2,0,5, 0,0,7]]
    # Super Difficult Sudoku, unsolvable by elimination method and requiring advanced techniques
    global h
    h = [[0,0,0, 0,0,0, 0,3,0],
         [6,0,5, 0,0,0, 0,0,0],
         [0,3,0, 0,1,0, 9,0,0],
         [5,7,0, 6,0,0, 0,0,0],
         [0,9,0, 0,0,0, 0,1,0],
         [0,0,0, 0,0,8, 0,2,4],
         [0,0,1, 0,7,0, 0,4,0],
         [0,0,0, 0,0,0, 5,0,8],
         [0,2,0, 0,0,0, 0,0,0]]
        # Correctly Formulated Sudoku
    global s6
    s6 = [[0,0,7, 0,0,0, 0,1,5],
          [0,0,0, 3,9,7, 0,8,0],
          [0,6,2, 0,1,8, 4,0,9], 
          [0,2,0, 0,0,1, 5,4,3],
          [7,0,0, 4,0,9, 0,0,1],
          [4,8,1, 2,0,0, 0,6,0],
          [9,0,6, 0,2,0, 7,3,0],
          [0,0,0, 9,8,4, 0,0,0],
          [1,5,0, 0,0,0, 2,0,0]]

# Check if a sudoku is solved
# If there are no zeros in a sudoku, the puzzle is solved
def solved(s):
    for row in s:
        if 0 in row:
            return False
    return True

# Given a row number x, a value to check val, and a sudoku puzzle s
# Return False if the given value has already been used in the indicated row, and True if the number is still available
def horizontalCheck(x, val, s):
    if val in s[x]:
        return False
    return True

# Given a column number y, a value to check val, and a sudoku puzzle s
# Returns False if the given value has already been used in the indicated column, and True if the number is still available
def verticalCheck(y, val, s):
    column = [i[y] for i in s]
    if val in column:
        return False
    return True

# Given the x and y position of the cell we are checking (column and row respectively)
# A value to check val, and a sudoku puzzle s
# Returns False if the given value has already been used in the indicated sub-square, and True if the number is still available
def subSquareCheck(x, y, val, s):
    # The coordinate of the upmost and leftmost point in the square we need
    column = x // 3 * 3; row = y // 3 * 3
    square = []
    for i in range(row, row+3):
        square.extend([s[i][j] for j in range(column, column+3)])
    if val in square:
        return False
    return True

# "Naked Singles" strategy
# Given a zero-indexed x and y position in the puzzle (column and row respectively), and a sudoku puzzle s
# Returns 0 if more than one possible answers, the answer if exactly one possible answer, and raises a "Sudoku Invalid" exception no possible answers
def elimination(x, y, s):
    ans = set(range(1, 10))
    for i in range(1, 10):
        if not horizontalCheck(y, i, s):
            ans.remove(i)
        elif not verticalCheck(x, i, s):
            ans.remove(i)
        elif not subSquareCheck(x, y, i, s):
            ans.remove(i)
    if len(ans) == 1:
        return ans.pop()
    elif len(ans) == 0:
        raise Exception('Sudoku Invalid')
    else:
        return 0

# Given a strategy and a puzzle s, applies that strategy to each cell in the puzzle
# Return True if the strategy worked, and False if it didn't
def applyStrategy(strategy, s):
    count = 0
    for y in range(9):
        for x in range(9):
            if s[y][x] == 0:
                result = strategy(x, y, s)
                if result != 0:
                    s[y][x] = result
                    count += 1
    if count == 0:
        return False
    return True

# Repeatedly apply the given list of strategies to the puzzle until they stop working or the puzzle is solved
def sudokuSolver(s, strategies):
    while not solved(s):
        work = []
        for i in strategies:
            result = applyStrategy(i, s)
            work.append(result)
        # any() function returns True if any item in an iterable is True, otherwise it returns False
        if not any(work):
            raise Exception('Sudoku Unsolvable')
    return s

# "Hidden Singles" strategy
# https://www.learn-sudoku.com/hidden-singles.html
def hiddenSingles(x, y, s):

    def mark(x, y, s): # The "pencil mark" of a cell
        ans = set(range(1, 10))
        for i in range(1, 10):
            if not horizontalCheck(y, i, s):
                ans.remove(i)
            elif not verticalCheck(x, i, s):
                ans.remove(i)
            elif not subSquareCheck(x, y, i, s):
                ans.remove(i)
        return ans

    target = mark(x, y, s)

    if len(target) == 1:
        return target.pop()
    elif len(target) == 0:
        raise Exception('Sudoku Invalid')
    else:
        rowM = set(); columnM = set(); subM = set()
        # Get marks for other empty cells in the same row
        for i in range(9):
            if i != x:
                if s[y][i] == 0:
                    cell = mark(i, y, s)
                    rowM.update(cell)
        # Get marks for other empty cells in the same column
        for j in range(9):
            if j != y:
                if s[j][x] == 0:
                    cell = mark(x, j, s)
                    columnM.update(cell)
        # Get marks for other empty cells in the same subsquare
        column = x // 3 * 3; row = y // 3 * 3
        for m in range(row, row+3):
            for n in range(column, column+3):
                if (m != y) or (n != x):
                    if s[m][n] == 0:
                        cell = mark(n, m, s)
                        subM.update(cell)

        for i in target:
            if i not in rowM:
                return i
            elif i not in columnM:
                return i
            elif i not in subM:
                return i
        return 0