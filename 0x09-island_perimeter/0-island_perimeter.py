#!/usr/bin/python3

def island_perimeter(grid):
    """determine the perimeter of an island"""
    count = 0
    print(f'len of grid {len(grid)}')
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if i == len(grid) - 1:
                    count += 1
                    if grid[j + 1][i] == 0:
                        count += 1
                    if grid[j - 1][i] == 0:
                        count += 1
                elif j == len(grid[i]) - 1:
                    count += 1
                    if grid[i + 1][j] == 0:
                        count += 1
                    if grid[i - 1][j] == 0:
                        count += 1
                else:
                    if grid[i][j+1] == 0:
                        count += 1
                    if grid[i][j-1] == 0:
                        count += 1
                    print(f'i is: {i}')
                    if grid[i + 1][j] == 0:
                        count += 1
                    if grid[i + 1][j] == 0:
                        count += 1
                print(f'count is: {count}')
                # else:
    return count
