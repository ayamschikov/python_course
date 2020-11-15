# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    if a >= b and b >= c:
        return a + b
    elif a >= b and c > b:
        return a + c
    else:
        return b + c


a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

print(my_func(a, b, c))
