# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(a, b):
    try:
        a = float(a)
        b = float(b)

        try:
            return a / b
        except ZeroDivisionError:
            return "Can't divide by zero"
    except ValueError:
        return "Arguments are not digits"


a = input('enter first argument: ')
b = input('enter second argument: ')

print(division(a, b))
