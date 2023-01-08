def largestInRow(i, row):
    l = i - 1
    largeL = 0
    while l > -1:
        largeL = max(largeL, row[l])
        l -= 1
    
    r = i + 1 
    largeR = 0
    while r < len(row):
        largeR = max(largeR, row[r])
        r += 1
    
    return (largeL, largeR)

def largestInCol(i, j, grid):
    up = i - 1  
    largeUp = 0
    while up > -1:
        largeUp = max(largeUp, grid[up][j])
        up -= 1
    
    down = i + 1 
    largeDown = 0
    while down < len(grid[0]):
        largeDown = max(largeDown, grid[down][j])
        down += 1
    
    return (largeUp, largeDown)

def visibleTrees(file):
    total = 0
    with open(file, 'r') as f:
        grid = []
        for line in f:
            row = []
            for l in line:
                if l.isnumeric():
                    row.append(int(l))
            grid.append(row)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i - 1 == -1 or i + 1 == len(grid) or j - 1 == -1 or j + 1 == len(grid[0]):
                    total += 1
                else:
                    left, right = largestInRow(j, grid[i])
                    up, down = largestInCol(i, j, grid)
                    if grid[i][j] > left or grid[i][j] > right or grid[i][j] > up or grid[i][j] > down:
                        total += 1
    
    return total

print(visibleTrees('day8_input.txt'))

def find(i, j, piece, grid):
    l = j - 1
    left = 0
    while l > -1:
        left += 1
        if grid[i][l] >= piece:
            break
        l -= 1
    
    r = j + 1
    right = 0
    while r < len(grid):
        right += 1
        if grid[i][r] >= piece:
            break
        r += 1
    
    u = i - 1
    up = 0
    while u > -1:
        up += 1
        if grid[u][j] >= piece:
            break
        u -= 1
    
    d = i + 1
    down = 0
    while d < len(grid[0]):
        down += 1
        if grid[d][j] >= piece:
            break
        d += 1

    return left * right * up * down



def highestScienicScore(file):
    highest = 0
    with open(file, 'r') as f:
        grid = []
        for line in f:
            row = []
            for l in line:
                if l.isnumeric():
                    row.append(int(l))
            grid.append(row)
        
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0]) - 1):
                highest = max(highest, find(i, j, grid[i][j], grid))
    return highest

print(highestScienicScore('day8_input.txt'))