# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
number = input('enter number for 4th task: ')
iterator = 0
max_digit = 0

while iterator < len(number):
    if int(number[iterator]) > max_digit:
        max_digit = int(number[iterator])
    iterator += 1

print(f'the biggest digit is {max_digit}')
