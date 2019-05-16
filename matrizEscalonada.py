#!/usr/bin/env python

def matrizEscalonada(A):
    
    filas = len(A)
    columnas = len(A[0])
   
    x = 0
    y = 0

    ciclos = filas if  filas <= columnas else columnas

    while x < ciclos and y < ciclos:
        # search and swap
        if A[x][y] == 0:
            for k in range(x+1, filas):
                if A[k][y] != 0:
                    tmp = list(A[k])
                    A[k] = list(A[x])
                    A[x] = list(tmp)
                    break
        # calculate
        if A[x][y] != 0:
            for m in range(x+1, filas):
                if A[m][y] != 0:
                    c = A[m][y] / A[x][y]
                    for n in range(y, columnas):
                        A[m][n] = A[m][n] - c * A[x][n]
            # move to next row only  if swap was successful
            x += 1
        y += 1
        
    # print matrix
    for x in range(filas):
        for y in range(columnas):
            print("%5.2f " % A[x][y], end="")
        print()

