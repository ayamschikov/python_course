# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]

new_element = int(input('enter new element: '))

print(f'initial list: {my_list}')

iterator = 0

# NOTE: made so to avoid sorting and reversing all list
while iterator < len(my_list):
    if new_element >= my_list[iterator] and iterator != len(my_list) - 1:
        my_list.insert(iterator, new_element)
        break
    elif iterator == len(my_list) - 1:
        my_list.insert(iterator + 1, new_element)
        break
    iterator += 1

print(f'new list: {my_list}')
