from time import sleep
from life_game_functions import clear_output_console
from life_game_functions import build_matrix2
from life_game_functions import evolve_matrix
from life_game_functions import print_matrix

# num_cols = int(input("¿Número de columnas?"))
# num_filas = int(input("¿Número de filas?"))
# num_pasos = input("¿Número de pasos?")

# configuration
num_pasos = 100
num_cols = 20
num_filas = 20

# initialize
# linea = build_line(int(num_cols))
# matrix = build_matrix(num_filas, linea, num_cols)
matrix = build_matrix2(num_filas, num_cols)

# assign test values

# matrix[8][8] = 1
# matrix[9][9] = 1
# matrix[10][9] = 1
# matrix[10][8] = 1
# matrix[10][7] = 1

matrix[9][8] = 1
matrix[9][9] = 1
matrix[9][10] = 1
# matrix[10][8] = 1
matrix[11][9] = 1
# matrix[10][10] = 1
matrix[11][8] = 1
matrix[11][10] = 1
matrix[10][9] = 1
matrix[10][7] = 1
matrix[10][11] = 1


print_matrix(matrix)
sleep(1)
for index in range(int(num_pasos)):
    clear_output_console(2)

    matrix = evolve_matrix(matrix, num_filas, num_cols)
    print_matrix(matrix)
    sleep(0.5)