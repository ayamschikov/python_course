# 7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.

# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:

# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

# Подсказка: использовать менеджер контекста.

with open('7.txt') as source_file:
    firms = {}
    firms_to_count = 0
    income_to_count = 0

    for line in source_file.readlines():
        firm_info = line.split()
        firm_income = int(firm_info[2]) - int(firm_info[3])
        firms[firm_info[0]] = firm_income

        if firm_income > 0:
            income_to_count += firm_income
            firms_to_count += 1

    result = [firms, {'average_profit': income_to_count / firms_to_count}]

print(result)