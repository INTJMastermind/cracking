# Compute the number of islands in a grid
import random

def makeGrid(size):
    grid = []
    for row in range(0, size):
        element = []
        for file in range(0, size):
            element.append(random.randint(0,1))
        grid.append(element)
    return grid

def getNeighbors(coord, size):
    # Returns the coordinate of the neighbors of a square. This includes diagonal neighbors.
    row = coord[0]
    file = coord[1] 

    possibleRows = [row-1, row, row+1]
    possibleFiles = [file-1, file, file+1]

    # Filter out the edge cases...
    filteredRows = []
    filteredFiles = []

    for r in possibleRows:
        if r >= 0 and r < size:
            filteredRows.append(r)

    for f in possibleFiles:
        if f >= 0 and f < size:
            filteredFiles.append(f)
    
    # Get all permutations of filteredRows and filteredFiles (except for the original square)
    neighbors = []

    for r in filteredRows:
        for f in filteredFiles:
            if [r, f] != [row, file]:   #exclude the original square
                neighbors.append([r, f])

    return(neighbors)

def getNeighbors2(coord, size):
    # Returns the coordinates of the neighbors of a square.
    # This looks only at square directly above/below or left/right.
    # Diagonal neighbors don't count.

    row = coord[0]
    file = coord[1] 
    possibles = [[row-1, file], [row+1, file], [row, file-1], [row, file+1]]
    neighbors = []

    for possible in possibles:
        if possible[0] >= 0 and possible[0] < size and possible[1] >= 0 and possible[1] < size:
            neighbors.append(possible)

    return(neighbors)

def checkGrid(coord, grid):
    # Checks the map grid at a coordinate.
    row = coord[0]
    file = coord[1] 
    return(grid[row][file])

def updateGrid(coord, grid):
    # Sets the grid's value at coord to "2",
    # which means that square is part of an already counted island.
    row = coord[0]
    file = coord[1] 
    grid[row][file] = 2
    return grid

def drawGrid(grid):
    # Draws the grid
    for row in grid: print(row)
    print("")

def recurseCoord(coord, grid, size):
    if checkGrid(coord, grid) == 1:
        grid = updateGrid(coord, grid)
        neighbors = getNeighbors2(coord, size)
        for neighbor in neighbors:
            recurseCoord(neighbor, grid, size)
    return grid

def islands(size):
    grid = makeGrid(size)
    #drawGrid(grid)
    counter = 0
    for x in range(0, size):
        for y in range(0, size):
            coord = [x, y]
            if checkGrid(coord, grid) == 1:
                counter += 1
                grid = recurseCoord(coord, grid, size)
                #print(counter)
                #drawGrid(grid)

    print("Number of islands is:")
    print(counter)
    return counter

islands(100)