# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список только числами.
# Класс-исключение должен контролировать типы данных элементов списка.

# Примечание: длина списка не фиксирована.
# Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.


class WrongNumberException(Exception):
    def __init__(self, value):
        self._value = value

    def __str__(self):
        return f"Wrong number: '{self._value}'"

    def __repr__(self):
        return self.__str__

def convert(number):
    try:
        number = float(number)
    except ValueError:
        raise WrongNumberException(number)
    return number

result = []

print("Enter 'stop' to exit")

while True:
    user_input = input("> ")

    if user_input == 'stop':
        break
    else:
        try:
            result.append(convert(user_input))
        except WrongNumberException as exception:
            print(exception)

print(f"result: {result}")
