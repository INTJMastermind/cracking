# Compute the number of islands in a grid
#import random

def makeGrid(numRows, numFiles):
    import random
    grid = []
    for _x in range(0, numRows):
        row = []
        for _y in range(0, numFiles):
            row.append(random.randint(0,1))
        grid.append(row)
    return grid

def getNeighbors8(coord):
    # Returns a set of coordinates of the neighbors of a square. This includes diagonal neighbors.
    row = coord[0]
    file = coord[1] 

    possibleRows = (row-1, row, row+1)
    possibleFiles = (file-1, file, file+1)

    # Get all permutations of filteredRows and filteredFiles.
    neighbors = set()
    for r in possibleRows:
        for f in possibleFiles:
            neighbors.add((r, f))

    neighbors.remove((row, file)) # Remove the original square

    return(neighbors)


def getNeighbors4(coord):
    # Returns a set of coordinates of the neighbors of a square.
    # This looks ONLY at squares directly above/below and left/right.
    # Diagonal neighbors don't count.

    row = coord[0]
    file = coord[1] 
    return {(row-1, file), (row+1, file), (row, file-1), (row, file+1)}


def checkGrid(coord, grid, numRows, numFiles):
    # Checks the map grid at a coordinate. Returns a value of '0' if the coordinate is outside the bounds of the grid.
    row = coord[0]
    file = coord[1] 

    if row < 0 or row >= numRows or file < 0 or file >= numFiles:
        return 0
    else:
        return(int(grid[row][file]))

def updateGrid(coord, grid):
    # Sets the grid's value at coord to "2", which indicates 
    # that square is part of an already counted island.
    row = coord[0]
    file = coord[1] 
    grid[row][file] = 2
    return

def drawGrid(grid):
    # Draws the grid
    for row in grid: print(row)
    print("")

def markIsland(coord, grid, numRows, numFiles):
    # Checks if neighbors of grid are land tiles ("1"), and if so, marks them as part
    # of an existing island ("2"), and recursively checks if *their* neighbors are also land tiles.
    # Note: We're passing numRows and numFiles because they're constants and not recalculating each time saves time.
    if checkGrid(coord, grid, numRows, numFiles) == 1:
        updateGrid(coord, grid)
        #neighbors = getNeighbors8(coord) # This version looks at 8 neighbors per square (diagonals included)
        neighbors = getNeighbors4(coord) # This version looks at 4 neighbors per square (diagonals not included)
        for neighbor in neighbors:
            markIsland(neighbor, grid, numRows, numFiles) # Recursively looks at the neighbors of that square to see if they're also land tiles.
    return

def islands(grid):
    # Defines the number of islands in a grid.
    numRows = len(grid)
    numFiles = len(grid[0])
    numIslands = 0
    for x, row in enumerate(grid): # Move through the grid and...
        for y, value in enumerate(row):
            if int(value) == 1:  # ...if we encounter a tile that is a land tile that's not part of an existing island ('1')...
                numIslands += 1 # ...increment the number of islands and...
                coord = (x, y)
                markIsland(coord, grid, numRows, numFiles) # ...recursively mark off all tiles that are part of that island.

    print(f"Number of islands is: {numIslands}")
    return numIslands

if __name__ == "__main__":
    grid = [["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]]
    drawGrid(grid)
    islands(grid)

    grid = [["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]]
    drawGrid(grid)
    islands(grid)

    grid = [[1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1]]
    drawGrid(grid)
    islands(grid)

    grid = makeGrid(10, 12)
    drawGrid(grid)
    islands(grid)