"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехала.'

    def stop(self):
        return f'Машина {self.name} остановилась.'

    def turn(self, direction):
        # direction = []
        return f'Машина {self.name} повернула - {direction}.'

    def show_speed(self):
        return f'Скорость {self.name}: {self.speed}.'

    def police_car(self):
        if self.is_police:
            return f'{self.name} - Police.'
        else:
            return f'{self.name} - не Police.'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        # print(f'Скорость {self.name}: {self.speed}')
        if self.speed > 60:
            return f'Машина {self.name} превысила скорость: {self.speed}, больше 60.'
        else:
            return f'Машина {self.name} не превысила скорость: {self.speed}.'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        # print(f'Скорость {self.name}: {self.speed}')
        if self.speed > 40:
            return f'Машина {self.name} превысила скорость: {self.speed}, больше 40.'
        else:
            return f'Машина {self.name} не превысила скорость: {self.speed}.'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


mazerati = SportCar(200, 'Red', 'Maserati', False)
lada = TownCar(45, 'Yellow', 'Лада', False)
bukhanka = WorkCar(80, 'White', 'Буханка', True)
audi_police = PoliceCar(150, 'Blue', 'Ауди', True)

print(mazerati.go(), mazerati.show_speed(), mazerati.turn('Налево'))
print(lada.go(), lada.show_speed(), lada.police_car())
print(bukhanka.go(), 'Цвет:', bukhanka.color, bukhanka.show_speed(), bukhanka.police_car())
print(audi_police.turn('Направо'), audi_police.show_speed(), audi_police.police_car(), audi_police.stop())
