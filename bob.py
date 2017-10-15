def leastRow(grid):
    least = 24 # holds sum of lowest moves to make row
    win = []
    
    # check diagonals
    tdiag = grid[0][0] + grid[1][1] + grid[2][2] # top left -> bottom right
    if tdiag < least:
        least = tdiag
        win = [[0, 0], [1, 1], [2, 2]]
    tdiag = grid[2][0] + grid[1][1] + grid[0][2] # bottom left -> top right
    if tdiag < least:
        least = tdiag
        win = [[2, 0], [1, 1], [0, 2]]

    # check row and col
    for x in range (0, 3):
        trow, tcol = 0, 0
        twinrow, twincol = [], []
        for y in range (0, 3):
            # temporary row
            trow += grid[x][y]
            twinrow.append([x, y])
            # temporary column
            tcol += grid[y][x]
            twincol.append([y, x])
        # check if row contains least win
        if trow < least:
            least = trow
            win = twinrow
        # check if col contains least win
        if tcol < least:
            least = tcol
            win = twincol
    return win

# get grid with move values
def getgrid(moves):
    grid = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    for i, move in enumerate(moves):
        grid[move[0]-1][move[1]-1] = i+1
    return grid

# get list of moves
moves = []
for line in range(0, 9):
    moves.append(map(int, raw_input().split()))

grid = getgrid(moves) # convert move list into grid
win = leastRow(grid) # get coordinates of the fastest win

# remove the winning moves from move list
for wmove in win:
    moves.remove([wmove[0]+1, wmove[1]+1])

moves.sort()

# print the first 3 ok moves
for i in range (0, 3):
    print str(moves[i][0]) + " " + str(moves[i][1])

