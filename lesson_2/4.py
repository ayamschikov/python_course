# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

entered_string = input('enter string: ').split()

iterator = 0
while iterator < len(entered_string):
    if len(entered_string[iterator]) > 10:
        print(f'{iterator}: {entered_string[iterator][0:10]}')
    else:
        print(f'{iterator}: {entered_string[iterator]}')

    iterator += 1
