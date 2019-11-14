def clear_output_console(lines):
    for index in range(lines):
        print("\n")

def build_line(positions):
    line = [0]
    if positions > 0:
        line.clear()
        for index in range(positions):
            line.append(0)
    return line

# lines builds on reference
def build_matrix(num_filas, linea, num_cols):
    m = [[0,0],[0,0]]
    # new_line = linea
    new_line = build_line(int(num_cols))

    if num_filas > 0:
        m.clear()
        for i in range(num_filas):
            m.append(new_line)

    return m

# lines builds on value
def build_matrix2(num_filas, num_cols):
    m = [[0, 0], [0, 0]]
    # new_line = linea
    new_line = build_line(int(num_cols))

    if num_filas > 0:
        m.clear()
        for i in range(num_filas):
            line = [0]
            if num_cols > 0:
                line.clear()
                for index in range(num_cols):
                    line.append(0)
            m.append(line)

    return m

def evolve_matrix(initial_matrix, mx_rows, mx_cols):
    # assign dimension
    new_matrix = build_matrix2(mx_rows, mx_cols)

    # initialize matrix with dummy values in order to evaluate whether all of its values have been assigned
    new_matrix = initialize_matrix(new_matrix, -1) # byref


    # evolve
    num_rows = len(initial_matrix)
    for row in range(num_rows):
        num_cols = len(initial_matrix[row])
        for column in range(num_cols):
            neighbours = 0
            row_previous = row - 1
            row_next = row + 1
            col_previous = column - 1
            col_next = column + 1

            if row_previous < 0:
                row_previous = num_rows - 1

            if row_next >= num_rows:
                row_next = 0

            if col_previous < 0:
                col_previous = num_cols - 1

            if col_next >= num_cols:
                col_next = 0

            above_left_value = initial_matrix[row_previous][col_previous]
            above_center_value = initial_matrix[row_previous][column]
            above_right_value = initial_matrix[row_previous][col_next]

            middle_left_value = initial_matrix[row][col_previous]
            middle_right_value = initial_matrix[row][col_next]

            below_left_value = initial_matrix[row_next][col_previous]
            below_center_value = initial_matrix[row_next][column]
            below_right_value = initial_matrix[row_next][col_next]

            neighbours = \
                above_left_value + above_center_value + above_right_value + \
                middle_left_value + middle_right_value + \
                below_left_value + below_center_value + below_right_value

            current_value = int(initial_matrix[row][column])
            if not str(current_value) == "0" and not str(current_value) == "1":
                current_value = 0

            new_status = 0
            if current_value == 1:
                if neighbours > 3 or neighbours < 2:
                    new_status = 0
                else:
                    new_status = 1
            else:
                # if neighbours == 2 or neighbours == 3:
                if neighbours == 3:
                    new_status = 1

            new_matrix[row][column] = new_status

    return new_matrix

def print_matrix(matrix):
    num_filas = len(matrix)
    for fila in range(num_filas):
        num_columnas = len(matrix[fila])

        cada_linea_a_mostrar = ""
        for columna in range(num_columnas):
            valor_a_mostrar = " "
            if matrix[fila][columna] == 1:
                valor_a_mostrar = "#"
            cada_linea_a_mostrar = "{} {}".format(cada_linea_a_mostrar, valor_a_mostrar)

        print("{}      {}".format(("00" + str(fila))[-2:], cada_linea_a_mostrar))

def initialize_matrix(m, v):
    num_rows = len(m)
    for row in range(num_rows):
        num_cols = len(m[row])
        for column in range(num_cols):
            m[row][column] = v
    return m
