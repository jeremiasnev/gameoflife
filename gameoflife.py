import cv2 as cv
import numpy as np

def CountNeighboursLand(grid, x, y):
    n = 0
    for i, row in enumerate(grid):
        if i <= y+1 and i >= y-1:
            for j, dot in enumerate(row):
                if j <= x+1 and j >= x-1:
                    if dot == 1:
                        n += 1
    n -= grid[y][x]
    return n

def DrawMap(map, width, height):
    img = np.zeros((height, width, 3), dtype=np.uint8)
    y=0
    for i in map:
        x=0
        for j in i:
            if j == 1:
                cv.rectangle(img,(x * 10, y * 10),( x * 10 + 9, y * 10 + 9),(255,255,255),1)
            elif j == 0:
                cv.rectangle(img,(x * 10, y * 10),( x * 10 + 9, y * 10 + 9),(0,0,0),1)
            x+=1
        y+=1
    cv.imshow("mesh", img)

def UpdateGrid(grid):
    gridRtn = []
    for i in range(len(grid)):
        row = []
        for j in range(len(grid[0])):
            row.append(0)
        gridRtn.append(row)
    print("Updating grid")
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            n = CountNeighboursLand(grid, j, i)
            if grid[i][j] == 0:
                if n == 3:
                    gridRtn[i][j] = 1
            elif grid[i][j] == 1:
                if n <= 1 or n >= 4:
                    gridRtn[i][j] = 0
                else:
                    gridRtn[i][j] = 1
    print("Updated")
    return gridRtn

def SetupGrid(size):
    size = 50

    grid = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(0)
        grid.append(row)
    return grid
    
gameOver = False
while not gameOver:
    DrawMap(grid, len(grid[0])*10, len(grid)*10)
    cv.waitKey(500)
    grid = UpdateGrid(list(grid))
cv.destroyAllWindows()