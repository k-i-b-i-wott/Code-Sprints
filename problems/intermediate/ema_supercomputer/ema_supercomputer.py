def is_valid_plus(grid, center_row, center_col, length):
    rows = len(grid)
    cols = len(grid[0])
    
    # Check if we can extend arms in all 4 directions
    for i in range(length):
        # Check up
        if center_row - i < 0 or grid[center_row - i][center_col] != 'G':
            return False
        # Check down
        if center_row + i >= rows or grid[center_row + i][center_col] != 'G':
            return False
        # Check left
        if center_col - i < 0 or grid[center_row][center_col - i] != 'G':
            return False
        # Check right
        if center_col + i >= cols or grid[center_row][center_col + i] != 'G':
            return False
    return True

def get_plus_coordinates(center_row, center_col, length):
    coordinates = set()
    # Add coordinates for all cells in the plus
    for i in range(length):
        coordinates.add((center_row - i, center_col))  # up
        coordinates.add((center_row + i, center_col))  # down
        coordinates.add((center_row, center_col - i))  # left
        coordinates.add((center_row, center_col + i))  # right
    return coordinates

def get_plus_area(length):
    # Area = (2 * length - 1)
    return (4 * length - 3)

def twoPluses(grid):
    if not grid:
        return 0
        
    rows = len(grid)
    cols = len(grid[0])
    max_product = 0
    
    # Find all possible pluses
    pluses = []
    for i in range(rows):
        for j in range(cols):
            length = 1
            while i - length + 1 >= 0 and i + length - 1 < rows and \
                  j - length + 1 >= 0 and j + length - 1 < cols:
                if is_valid_plus(grid, i, j, length):
                    coords = get_plus_coordinates(i, j, length)
                    area = get_plus_area(length)
                    pluses.append((coords, area))
                length += 1
    
    # Find maximum product of two non-overlapping pluses
    for i in range(len(pluses)):
        for j in range(i + 1, len(pluses)):
            plus1_coords, plus1_area = pluses[i]
            plus2_coords, plus2_area = pluses[j]
            
            if not plus1_coords.intersection(plus2_coords):
                max_product = max(max_product, plus1_area * plus2_area)
    
    return max_product
