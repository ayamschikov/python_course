# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

try:
    script_name, hours_count, rate_per_hour, bonus = argv

    income = int(hours_count) * int(rate_per_hour) + int(bonus)
    print(f'income = {income}')
except ValueError:
    print('Params error. You need to pass 3 integer params: hours_count, rate_per_hour, bonus')

