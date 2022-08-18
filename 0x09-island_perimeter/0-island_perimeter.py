#!/usr/bin/python3

def island_perimeter(grid):
    """determine the perimeter of an island"""
    count = 0
    print(f'len of grid {len(grid)}')
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                count += 4
                if i > 0 and grid[i-1][j] == 1:
                    count -= 2
                if j > 0 and grid[i][j-1] == 1:
                    count -=2
    return count
