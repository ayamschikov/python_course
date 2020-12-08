# 6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

from task4 import Copier, Printer, Scanner
from task5 import Storage

storage = Storage(2)
copier = Copier('Model 2')
printer = Printer('Model 23')

storage.add_equipment(copier)
storage.add_equipment(printer)

print(storage)

storage.get_equipment('Scanner')
storage.get_equipment('Printer')

print(storage)
