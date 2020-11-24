# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('1.txt', 'w') as my_file:
    while True:
        user_text = input('enter some text: ')
        if user_text == '':
            break
        print(user_text, file=my_file)
