# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: см. в методичке.

# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
# первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix: [[int]]):
        self._matrix = matrix
        self._rows_count = len(matrix)
        self._columns_count = len(matrix[0])

    def __str__(self):
        string = ''

        for row in self._matrix:
            for cell in row:
                string += str(cell) + "\t"
            string += "\n"

        return string

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise Exception("Can't add matrix with different object that is not matrix")

        if self._rows_count != other._rows_count or self._columns_count != other._columns_count:
            raise Exception("Can't add matrix with different rows/columns count")

        new_matrix = []
        for i in range(self._rows_count):
            row = []
            for j in range(self._columns_count):
                row.append(self._matrix[i][j] + other._matrix[i][j])
            new_matrix.append(row)

        return Matrix(new_matrix)

first_matrix = Matrix([[1, 2], [3, 4]])
second_matrix = Matrix([[5, 6], [7, 8]])

print('first_matrix')
print(first_matrix)

print('second_matrix')
print(second_matrix)

print('matrix add')
print(first_matrix + second_matrix)
