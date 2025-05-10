def gridCleaner(grid, column, row, n, dir=0):
    
    grid = [row[:] for row in grid]
    
    
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    for _ in range(n):
        
        current_state = grid[row][column]
        
        
        if current_state == 1:  # Clean (white) cell
            dir = (dir + 1) % 4  # Turn right
        else: 
            dir = (dir - 1) % 4  # Turn left
        
        
        grid[row][column] = 1 - current_state
        
       
        dy, dx = directions[dir]
        row += dy
        column += dx
        
      
        if row < 0:
            grid.insert(0, [0] * len(grid[0]))
            row = 0
        elif row >= len(grid):
            grid.append([0] * len(grid[0]))
        if column < 0:
            for r in grid:
                r.insert(0, 0)
            column = 0
        elif column >= len(grid[0]):
            for r in grid:
                r.append(0)
    
    return grid