# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

with open('2.txt') as my_file:
    iterator = 1
    for line in my_file.readlines():
        words_count = len(line.split(' '))
        print(f'line #{iterator} has {words_count} symbols')
        iterator += 1
    print(f"lines total: {iterator - 1}")
