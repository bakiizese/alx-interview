#!/usr/bin/python3


def island_perimeter(grid):
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Add 4 for the current land cell
                perimeter += 4
                
                # Subtract 1 for each neighboring land cell
                if r > 0 and grid[r - 1][c] == 1:  # Check above
                    perimeter -= 1
                if r < rows - 1 and grid[r + 1][c] == 1:  # Check below
                    perimeter -= 1
                if c > 0 and grid[r][c - 1] == 1:  # Check left
                    perimeter -= 1
                if c < cols - 1 and grid[r][c + 1] == 1:  # Check right
                    perimeter -= 1
    
    return perimeter
