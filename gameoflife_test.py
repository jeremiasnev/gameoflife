import cv2 as cv
import numpy as np
import random as rand

def CountNeighboursLand(grid, x, y):
    ninjat = 0
    for i, row in enumerate(grid):
        if i <= y+1 and i >= y-1:
            for j, dot in enumerate(row):
                if j <= x+1 and j >= x-1:
                    if dot == 1:
                        ninjat += 1
    ninjat -= grid[y][x]
    return ninjat


def DrawMap(map, width, height, save=""):
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
    if save != "":
        cv.imwrite(save, img)
        print(save, " saved")

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

def RandomFill(grid, percent):
    gridRtn = []
    for i in range(len(grid)):
        row = []
        for j in range(len(grid[0])):
            if rand.random() > percent:
                row.append(0)
            else:
                row.append(1)
        gridRtn.append(row)
    return gridRtn

mapSize = 50

grid = []
for i in range(mapSize):
    row = []
    for j in range(mapSize):
        row.append(0)
    grid.append(row)

fillStyle = int(input("Fillstyle: "))
if fillStyle == 1:
    percent = float(input("Fillpercent: "))
    grid = RandomFill(grid, percent)
elif fillStyle == 2:
    grid[5][5] = 1
    grid[5][6] = 1
    grid[5][7] = 1
    grid[6][7] = 1
    grid[7][6] = 1

    grid[5 + 5][5 + 5] = 1
    grid[5 + 5][6 + 5] = 1
    grid[5 + 5][7 + 5] = 1
    grid[6 + 5][7 + 5] = 1
    grid[7 + 5][6 + 5] = 1

    grid[5 + 10][5] = 1
    grid[5+ 10][6] = 1
    grid[5 + 10][7] = 1
    grid[6 + 10][7] = 1
    grid[7 + 10][6] = 1
elif fillStyle == 3:
    inX = 0
    inY = 0
    while inX >= 0:
        DrawMap(grid, mapSize*10, mapSize*10)
        cv.waitKey(100)
        inX = int(input("X cord to change: "))
        inY = int(input("Y cord to change: "))
        if grid[inY][inX] == 1:
            grid[inY][inX] == 0
        else:
            grid[inY][inX] = 1


DrawMap(grid, mapSize*10, mapSize*10)
cv.waitKey(0)
gameOver = False
while not gameOver:
    DrawMap(grid, mapSize*10, mapSize*10)
    cv.waitKey(400)
    grid = UpdateGrid(list(grid))
cv.destroyAllWindows()

