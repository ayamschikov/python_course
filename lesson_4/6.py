# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count, cycle
from sys import argv

try:
    script_name, start_number = argv

    iterator = 0

    print('----------------')
    print('count')

    for el in count(int(start_number)):
        print(el)
        if iterator >= 10:
            break
        iterator += 1
except ValueError:
    print('Params error. You need to pass integer param: start_number')

print('----------------')
print('cycle')

def cycle_list():
    iterator = 0

    for el in cycle((300, 2, 12)):
        print(el)
        if iterator > 10:
            break
        iterator += 1

cycle_list()
