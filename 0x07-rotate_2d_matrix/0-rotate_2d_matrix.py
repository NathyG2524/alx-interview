#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    newMatrix = []
    newArray = []
    lastMatrix = []
    # for i in matrix:
    #     newMatrix.append(newArray)
    for i in range(len(matrix)):
        newArray = []
        for j in range(len(matrix[i])):
            newNum = matrix[i][j]
            newArray.append(newNum)
        newMatrix.append(newArray)
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            newMatrix[j][i] = matrix[i][j]
    
    for i in range(len(newMatrix)):
        newArray = []
        for j in range(len(newMatrix[i])):
            newNum = newMatrix[i][j]
            newArray.append(newNum)
        lastMatrix.append(newArray)

    for i in range(len(newMatrix)):
        k = 0
        for j in range(len(newMatrix[i])):
            n = len(matrix[i]) - 1
            lastMatrix[i][n - k] = newMatrix[i][j]
            k += 1
            
        print(n) 
    print(lastMatrix)