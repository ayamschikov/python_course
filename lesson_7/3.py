# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.

class OrganicCell(object):
    def __init__(self, nucleus_count: int):
        self._nucleus_count = nucleus_count

    def __add__(self, other):
        if not isinstance(other, OrganicCell):
            raise Exception("Can't operate with object that is not OrganicCell")

        return OrganicCell(self._nucleus_count + other._nucleus_count)

    def __sub__(self, other):
        if not isinstance(other, OrganicCell):
            raise Exception("Can't operate with object that is not OrganicCell")

        new_nucleus_count = self._nucleus_count - other._nucleus_count

        if new_nucleus_count > 0:
            return OrganicCell(new_nucleus_count)
        else:
            print('Cell count is negative')
            return None

    def __mul__(self, other):
        if not isinstance(other, OrganicCell):
            raise Exception("Can't operate with object that is not OrganicCell")

        return OrganicCell(self._nucleus_count * other._nucleus_count)

    def __truediv__(self, other):
        if not isinstance(other, OrganicCell):
            raise Exception("Can't operate with object that is not OrganicCell")

        return OrganicCell(self._nucleus_count // other._nucleus_count)

    def __str__(self):
        return f"OrganicCell has {self._nucleus_count} nucleus"

    def __repr__(self):
        return self.__str__()

    def make_order(self, cell_count: int):
        if cell_count < 1:
            raise Exception("Cell count must be greater than 0")

        for i in range(self._nucleus_count // cell_count):
            print("*" * cell_count)

        print('*' * (self._nucleus_count % cell_count))
        return ''

first_cell = OrganicCell(8)
second_cell = OrganicCell(2)

print(f"First cell: {first_cell}")
print(f"Second cell: {second_cell}\n")

print(f"Sum of cells: {first_cell + second_cell}")
print(f"Subtraction of cells: {first_cell - second_cell}")
print(f"Multiplication of cells: {first_cell * second_cell}")
print(f"Division of cells: {first_cell / second_cell}\n")

print(f"Order by 5 of first_cell:")
first_cell.make_order(5)
print(f"Order by 1 of second_cell:")
second_cell.make_order(1)
