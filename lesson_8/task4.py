# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class OfficeEquipment:
    title: str

    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Equipment title - '{self.title}'\nMy specialization is {self.specialization}"

    def __repr__(self):
        return self.__str__()

class Printer(OfficeEquipment):
    def __init__(self, title):
        self.specialization = "print"
        return super().__init__(title)


class Scanner(OfficeEquipment):
    def __init__(self, title):
        self.specialization = "scan"
        return super().__init__(title)

class Copier(OfficeEquipment):
    def __init__(self, title):
        self.specialization = "copy"
        return super().__init__(title)
