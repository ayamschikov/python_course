# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    day: int
    month: int
    year: int

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def parse(cls, date):
        parts = date.split('-')

        if len(parts) != 3:
            raise Exception("Wrong date format")

        for part in parts:
            if not part.isdigit():
                raise Exception(f"Part '{part}' must be digit")

        day, month, year = [int(x) for x in parts]
        Date._validate(day, month, year)

        return Date(day, month, year)

    @staticmethod
    def _validate(day: int, month: int, year: int):
        if day < 1 or day > 31:
            raise Exception(f"Number of day is not correct '{day}'")
        if month < 1 or month > 12:
            raise Exception(f"Number of month is not correct '{month}'")
        return True


    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __repr__(self):
        return self.__str__

dates = ['23-02-2000', '18-12-1951']

print(Date.parse(dates[0]))
print(Date.parse(dates[1]))

