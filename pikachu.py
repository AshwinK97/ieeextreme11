
def path(row, col, grid):
    minhealth = 100
    health = 0
    row, col = row-1, col-1 # bottom right
    r, c = 0, 0 # top left
    while r < row or c < col:
        health += grid[r][c]
        if health < minhealth:
            minhealth = health 
        if r+1 <= row:
            if c+1 <= col:
                if grid[r+1][c] >= grid[r][c+1]:
                    r+=1
                else:
                    c+=1
            else:
                r+=1
        elif c+1 <= col:
            c+=1

    return minhealth * (-1) + 1

# get input
row, col = map(int, raw_input().split())
grid = []
for i in range (0, row):
    grid.append(map(int, raw_input().split()))

print path(row, col, grid)
