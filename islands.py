# Compute the number of islands in a grid
import random

def makeGrid(size):
    grid = []
    for _x in range(0, size):
        row = []
        for _y in range(0, size):
            row.append(random.randint(0,1))
        grid.append(row)
    return grid

def getNeighbors(coord, size):
    # Returns a list of coordinates of the neighbors of a square. This includes diagonal neighbors.
    row = coord[0]
    file = coord[1] 

    possibleRows = (row-1, row, row+1)
    possibleFiles = (file-1, file, file+1)

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
            if (r, f) != (row, file):   #exclude the original square
                neighbors.append((r, f))

    return(neighbors)

def getNeighbors2(coord, size):
    # Returns a list of coordinates of the neighbors of a square.
    # This looks only at square directly above/below or left/right.
    # Diagonal neighbors don't count.

    row = coord[0]
    file = coord[1] 
    possibles = [(row-1, file), (row+1, file), (row, file-1), (row, file+1)]
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

def markIsland(coord, grid, size):
    # Checks if neighbors of grid are land tiles ("1"), and if so, marks them as part
    # of an existing island ("2"), and recursively checks if *their* neighbors are also land tiles.
    if checkGrid(coord, grid) == 1:
        updateGrid(coord, grid)
        #neighbors = getNeighbors(coord, size) # This version looks at 8 neighbors per square (diagonals included)
        neighbors = getNeighbors2(coord, size) # This version looks at 4 neighbors per square (diagonals not included)
        for neighbor in neighbors:
            markIsland(neighbor, grid, size) # Recursively looks at the neighbors of that square to see if they're also land tiles.
    return

def islands(size):
    grid = makeGrid(size)
    drawGrid(grid)
    numIslands = 0
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if value == 1:  # If the tile at (x,y) is a land tile that's not part of an existing island...
                numIslands += 1
                coord = (x, y)
                markIsland(coord, grid, size) # Recursively mark off all tiles that are part of that island.

    print(f"Number of islands is: {numIslands}")
    return numIslands

if __name__ == "__main__":
    islands(10)