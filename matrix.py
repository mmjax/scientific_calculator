import numpy as np


def input_matrix():
    while True:
        print("Какую операцию с матрицами вы хотите выполнить\n1.Сложение\n2.Вычитание\nq чтобы выйти")
        choice = input()
        if choice == 'q':
            break
        print("Для начала введите первую матрицу:")
        matrix1 = []
        matrix2 = []
        while True:
            line = input()
            if line == 'end':
                break
            try:
                matrix1.append([int(k) for k in line.split()])
            except:
                break
        print("Введите вторую матрицу:")
        while True:
            line = input()
            if line == 'end':
                break
            try:
                matrix2.append([int(k) for k in line.split()])
            except:
                break
        if choice == '1':
            result = add_matrix(matrix1, matrix2)
            for row in result:
                print(" ".join(map(str, row)))
        elif choice == '2':
            subtract_matrix(matrix1, matrix2)



def add_matrix(matrix1, matrix2):
    result = np.add(matrix1, matrix2)
    return result
def subtract_matrix(matrix1, matrix2):
    result = np.subtract(matrix1, matrix2)
    for row in result:
        print(" ".join(map(str, row)))
    return result