# Compute the number of islands in a grid

def make_grid(num_rows, num_cols):
    import random
    return [[random.randint(0,1) for _col in range(0, num_cols)] for _row in range(0, num_rows)]


def get_neighbors8(coord):
    # Returns a set of coordinates of the neighbors of a square. This includes diagonal neighbors.
    row = coord[0]
    col = coord[1] 

    possible_rows = (row-1, row, row+1)
    possible_cols = (col-1, col, col+1)

    # Get all permutations of filteredRows and filteredFiles.
    neighbors = {(r,c) for c in possible_cols for r in possible_rows}
    neighbors.remove((row, col)) # Remove the original square
    return(neighbors)


def get_neighbors4(coord):
    # Returns a set of coordinates of the neighbors of a square.
    # This looks ONLY at squares directly above/below and left/right.
    # Diagonal neighbors don't count.
    row = coord[0]
    col = coord[1] 
    return {(row-1, col), (row+1, col), (row, col-1), (row, col+1)}


def check_grid(coord, grid, num_rows, num_cols):
    # Checks the map grid at a coordinate. Returns a value of '0' if the coordinate is outside the bounds of the grid.
    row = coord[0]
    col = coord[1] 
    if row < 0 or row >= num_rows or col < 0 or col >= num_cols:
        return 0
    else:
        return(int(grid[row][col]))  # Convert to integer to take into account strings


def draw_grid(grid):
    # Draws the grid
    for row in grid: print(row)
    print("")


def mark_island(coord, grid, num_rows, num_cols):
    # Checks if a grid is previously unvisited land tile ("1"), and if so, marks them as part
    # of the existing island ("2"), and recursively checks if their neighbors are also land tiles.
    # Note: We're passing num_rows and num_cols because they're constants and not recalculating each time saves time.
    if check_grid(coord, grid, num_rows, num_cols) == 1:
        grid[coord[0]][coord[1]] = 2    # Sets the grid's value at coord to "2", which indicates that square is part of an already counted island.
        neighbors = get_neighbors8(coord) # This version looks at 8 neighbors per square (diagonals included)
        #neighbors = get_neighbors4(coord) # This version looks at 4 neighbors per square (diagonals not included)
        for neighbor in neighbors:
            mark_island(neighbor, grid, num_rows, num_cols) # Recursively looks at the neighbors of that square to see if they're also land tiles.


def islands(grid):
    # Defines the number of islands in a grid.
    num_rows = len(grid)
    num_cols = len(grid[0])
    num_islands = 0
    for x, row in enumerate(grid): # Move through the grid and...
        for y, value in enumerate(row):
            if int(value) == 1: # ...if we encounter a tile that is a land tile that's not part of an existing island ('1')...
                num_islands += 1 # ...increment the number of islands and...
                mark_island((x, y), grid, num_rows, num_cols) # ...recursively mark off all tiles that are part of that island.

    print(f"Number of islands is: {num_islands}\n")
    return num_islands


if __name__ == "__main__":
    grid = [["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]]
    draw_grid(grid)
    islands(grid)

    grid = [["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]]
    draw_grid(grid)
    islands(grid)

    grid = [[1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1]]
    draw_grid(grid)
    islands(grid)

    grid = [[1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]]
    draw_grid(grid)
    islands(grid)

    grid = make_grid(6, 6)
    draw_grid(grid)
    islands(grid)