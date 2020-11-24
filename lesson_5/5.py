# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

with open('5.txt', 'w') as source_file:
    iterator = 0
    while iterator < 10:
        print(randint(0, 1000), file=source_file, end=' ')
        iterator += 1

with open('5.txt') as source_file:
    numbers = [int(number) for number in source_file.readline().split()]
    print(f'generated numbers: {numbers}')
    print(f'numbers sum: {sum(numbers)}')
