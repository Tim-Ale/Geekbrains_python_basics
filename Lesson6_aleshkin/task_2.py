"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    # length 5000m
    __length = None
    # width 20m
    __width = None
    # weight 25kg
    weight = None
    # thickness 5cm = 0.05m
    thickness = None

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def mass_calc(self):
        self.weight = 25
        self.thickness = 0.05
        # Total mass, kg -> t
        mass_calc = self.length * self.width * self.weight * self.thickness / 1000
        print(f'Масса асфальта: {mass_calc}, т')


my_road = Road(5000, 20)
my_road.mass_calc()
