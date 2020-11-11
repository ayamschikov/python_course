# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
income = int(input('enter income: '))
expenses = int(input('enter expenses: '))

if income > expenses:
    print('you earned money!')
    print('income to expenses ratio = {}'.format(income / expenses))
    employees_count = int(input('enter count of employees: '))
    print('your income by employee = {}'.format((income - expenses) / employees_count))
elif income == expenses:
    print('at least you have not lost money')
else:
    print('you lost some money')
