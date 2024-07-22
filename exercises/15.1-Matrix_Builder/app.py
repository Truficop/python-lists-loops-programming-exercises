# Your code here
def matrix_builder(entero):
    new_list = []
    for i in range(entero):
        linea = []
        for j in range(entero):
            linea.append(1)
        new_list.append(linea)
    return new_list

print(matrix_builder(3))
