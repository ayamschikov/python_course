# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

list_to_change = input("enter elements, separated by space (' '): ").split()

print('original list')
print(list_to_change)

iterator = 0
while iterator < len(list_to_change):
    if iterator != len(list_to_change) - 1:
        list_to_change[iterator], list_to_change[iterator + 1] = list_to_change[iterator + 1], list_to_change[iterator]
    iterator += 2

print('changed list')
print(list_to_change)
