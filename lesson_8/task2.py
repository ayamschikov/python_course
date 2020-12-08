# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyZeroDivisionException(ZeroDivisionError):
    def __init__(self):
        pass

    def __str__(self):
        return 'You tried to divide by zero'

    def __repr__(self):
        return self.__str__

# NOTE: не работает, не понял как сделать
try:
    5 / 0
except MyZeroDivisionException as exception:
    print(exception)
