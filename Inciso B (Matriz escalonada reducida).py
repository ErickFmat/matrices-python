### Funciones ###
def imprimir_matriz(matriz):

    # Determinar dimensiones de la matriz introducida
    numero_filas = len(matriz)
    numero_columnas = len(matriz[0])

    for i in range(numero_filas):
        for j in range(numero_columnas):
            print("[%5.2f]" % matriz[i][j], end="")
        print()

def matriz_escalonada_reducida(A):
    
    # Determinar dimensiones de la matriz introducida
    numero_filas = len(A)
    numero_columnas = len(A[0])

    x = 0
    y = 0

    # DOCUMENTAR 
    ciclos = numero_filas if (numero_filas <= numero_columnas) else numero_columnas

    while (x < ciclos) and (y < ciclos):
      # Buscar e intercambiar DOCUMENTAR
      if A[x][y] == 0:
          for k in range(x+1, numero_filas):
              if A[k][y] != 0:
                  tmp = list(A[k])
                  A[k] = list(A[x])
                  A[x] = list(tmp)
                  break

      # Calcular DOCUMENTAR 
      if A[x][y] != 0:
          # change pivot value to 1
          c = 1/A[x][y]
          for m in range(y, numero_columnas):
              A[x][m] *= c
          
          # convert remaining values above the pivot to 0
          for m in range(0, x):
              if A[m][y] != 0:
                  c = -A[m][y]
                  for n in range(y, numero_columnas):
                      A[m][n] = A[m][n] + c * A[x][n]
          
          # convert remaining values below the pivot to 0
          for m in range(x+1, numero_filas):
              if A[m][y] != 0:
                  c = -A[m][y]
                  for n in range(y, numero_columnas):
                      A[m][n] = A[m][n] + c * A[x][n]

          x += 1
      y += 1


### Main ###
print("Programa que determina la forma escalonada reducida de una matriz A.\n")

# Leer las dimensiones de la matriz
numero_filas = int(input("Introduzca la cantidad de filas de A: "))
numero_columnas = int(input("Introduzca la cantidad de columnas de A: "))

# Inicializar lista vacía
matriz_A = []

# Leer matriz A
print("")
for i in range(numero_filas):
    matriz_A.append([])
    for j in range(numero_columnas):
        matriz_A[i].append(
            float(input("Introduzca el elemento [%d][%d]: " % (i + 1, j + 1))))

print("\nMatriz introducida:\n")
imprimir_matriz(matriz_A)

print("\nMatriz en forma escalonada reducida:\n")
matriz_escalonada_reducida(matriz_A)
imprimir_matriz(matriz_A)
