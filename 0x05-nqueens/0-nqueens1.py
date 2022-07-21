#!/usr/bin/python3
from sys import argv
# from tabnanny import che/ck

from flask_restful import abort


def validation():
    value = True
    if len(argv) > 2:
        value = False
        print("Usage: nqueens N")
    try:
        n = int(argv[1])
    except:
        value = False
        print("N must be a number")
        
    if n < 0:
        value = False
        print("N must be at least 4")
    
    if value:
        return n
    return value

def board():
    try:
        if validation():
            n = validation()
            board = []
            for i in range(n):
                board_row = []
                for j in range(n):
                    board_row.append(0)
                board.append(board_row)
    except:
        abort

    return board

def checkForSpot(bor, col):
    row = {
        'valid': True,
        'value': col
        }
    # check row
    for i in range(len(bor[col])):   
        if bor[col][i] == 1:
            row = {
            'valid': False,
            'value': None
            }
    return row

def checkCol(bor, col, r):
    col = {
            'valid': True,
            'value': r
            }
    for i in range(n):
        if bor[i][r] == 1:
            col = {
            'valid': False,
            'value': None
            }
    return col
def getDia( col, row):
    #check for diagonal
    # diagonals_list = []
    # diagonals = {}
    # if col or row == 0 or n:
    #     d = {'col': col, 'row':row}
    #     diagonals.update(d)
    # for k, v in diagonals.items():
    # diagonals[colu] = col + 1
    # diagonals[rows ] = col + 1
    column = []
    rows = []
    colu = col
    ro = row 
    print(f'col: {col} row: {row}')
# for i in range(n):
    #check for the lower right diagonals
    while (-1< int(colu) < n) and (-1 < int(ro) < n):
        colu = colu + 1
        ro = ro + 1
        if colu == -1 or ro == -1 or colu == n  or ro == n :
            pass
        else:
            
            column.append(colu)
            rows.append(ro)
    
    #check for upper left diagonals
    colu1 = col
    ro1 = row
    while (-1< colu1 < n) and (-1 < ro1 < n):
        colu1 = colu1 - 1
        ro1 = ro1 - 1
        if colu1 == -1 or ro1 == -1 or colu1 == n  or ro1 == n :
            pass
        else:
            
            column.append(colu1)
            rows.append(ro1)

    #check for upper right diagonals
    colu2 = col
    ro2 = row
    while (-1< colu2 < n) and (-1 < ro2 < n):
        colu2 = colu2 - 1
        ro2 = ro2 + 1
        if colu2 == -1 or ro2 == -1 or colu2 == n  or ro2 == n :
            pass
        else:
            
            column.append(colu2)
            rows.append(ro2)

    #check for lower left diagonals
    colu3 = col
    ro3 = row
    while (-1< colu3 < n) and (-1 < ro3 < n):
        colu3 = colu3 + 1
        ro3 = ro3 - 1
        if colu3 == -1 or ro3 == -1 or colu3 == n  or ro3 == n :
            pass
        else:
            
            column.append(colu3)
            rows.append(ro3)
            # getDia(bor, colu, ro)
        # d = {'col': col, 'row':row}
        # diagonals.update(d)
    print(column)
    print(rows)
    # for i in range(len(column)):
    #     diagonals[column[i]] = rows[i]
    # for c, r in zip(column, rows)  :
    #     print(f'diagonals {c},{r}') 
    # print(list(diagonals))
    return {
        "col": column,
        "row": rows
    }

def checkDia(col, row):
    dia = {
                'valid': True
                }
    for i in range(len(col) - 1):
        if bor[col[i]][row[i]] == 1:
            dia = {
                'valid': False
                }
    return dia

def getFreeSpot(bor, col):
    row  = checkForSpot(bor, col)

    freeR = None
    free = None
    if row.get("valid"):
        freeR = row.get('value')
        coln = checkCol(bor, col, freeR)
        if coln.get("valid"):
            free = coln.get('value')
            # print(f'free col {freeR} ---- free row {freeR}')
            
            
    return {
            "col": freeR,
            "row": free
            }

bor = board()
n = validation()





# def assignQ():
for i in range(n):
    spot = getFreeSpot(bor, i)
    freeR =spot.get('col')
    free = spot.get('row')
    dia = getDia( 2, 4)
    free = 4
    columnD = dia.get('col')
    rowD = dia.get('row')
    # print(columnD)
    print(checkDia(columnD, rowD).get("valid"))
    while checkDia(columnD, rowD).get("valid"):
        print(checkDia(columnD, rowD).get("valid"))

        free = free + 1
        
        if free < n:
            
            dia = getDia( freeR, free)
            # columnD = dia.get('col')
            rowD = dia.get('row')
            
            bor[freeR][free] = 1
            print(free)
        else:
            break
for i in bor:
    print(i)