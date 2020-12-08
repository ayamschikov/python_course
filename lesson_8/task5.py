# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.

class Storage:
    equipments: dict
    max_place: int

    def __init__(self, max_place):
        self.max_place = max_place
        self.equipments = {}

    def add_equipment(self, equipment):
        if len(self.equipments) == self.max_place:
            print(f"Can't add new equipment, storage is full (limit: {self.max_place})\n")
            return None

        equipment_type = str(type(equipment).__name__)

        if equipment_type in self.equipments:
            self.equipments[equipment_type].append(equipment)
        else:
            self.equipments[equipment_type] = []
            self.equipments[equipment_type].append(equipment)

    def get_equipment(self, equipment_type):
        if equipment_type in self.equipments:
            return self.equipments[equipment_type].pop()
        else:
            print(f"I don't have a {equipment_type}\n")

    def __str__(self):
        if self.equipments:
            status = f"Currently I have (max storage {self.max_place})\n"
            for equipment_type, equipments in self.equipments.items():
                status += f"{len(equipments)} {equipment_type}\n"
        else:
            status = "Currently I'm empty"
        return status

    def __repr__(self):
        return self.__str__
