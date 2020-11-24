# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4

# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

import re

dictionary = {
        "One": "Один",
        "Two": "Два",
        "Three": "Три",
        "Four": "Четыре"
        }

with open('4.txt') as source_file:
    with open('4_modified.txt', 'w') as destination_file:
        for line in source_file.readlines():
            word_to_change = re.match('\w+', line)
            if word_to_change:
                line_to_write = line.replace(word_to_change.group(0), dictionary[word_to_change.group(0)]).replace('\n', '')
            else:
                line_to_write = line.replace('\n', '')

            print(line_to_write, file=destination_file)

print('Done')
