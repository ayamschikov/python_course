# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:

# Иванов 23543.12
# Петров 13749.32

with open('3.txt') as my_file:
    employees = {}
    for line in my_file.readlines():
        employee = line.split(' ')
        employees[employee[0]] = float(employee[1])

poor_payed_employees = [ name for name in employees.keys() if employees[name] < 20000 ]
average_salary = sum([ val for val in employees.values() ]) / len(employees)

print(f'employees who have less than 20k: {poor_payed_employees}')
print(f'average_salary: {average_salary}')
