"""
Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина). Значения данных атрибутов должны передаваться
при создании экземпляра класса. Атрибуты сделать защищенными. Определить
метод расчета массы асфальта, необходимого для покрытия всего дорожного
полотна.

Использовать формулу:
    (длина * ширина * масса асфальта) для покрытия одного кв метра дороги
    асфальтом, толщиной в (1 см * число см толщины полотна).

Проверить работу метода.

Например: 20м*5000м*25кг*5см = 12500 т
"""

class Road:
    __length = None
    __width = None
    weigth = None
    tickness = None
    def __init__(self, length, width):
        self.length = length
        self.width = width
        print('Строительство объекта "поселковая дорога":')

    def intake(self):
        self.weigth = 25
        self.tickness = 0.1
        intake = self.length * self.width * self.weigth * self.tickness / 1000
        print(f"Необходимо {intake} тонн для строительства объекта.")

road_to_village = Road(10000, 7)
road_to_village.intake()