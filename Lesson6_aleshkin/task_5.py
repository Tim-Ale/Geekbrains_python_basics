"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title='Канцелярская Принадлежность'):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки.'


class Pen(Stationery):
    def draw(self):
        # title = 'Ручкой'
        return f'Отрисовка {self.title}.'


class Pencil(Stationery):
    def draw(self):
        # title = 'Карандашом'
        return f'Отрисовка {self.title}.'


class Handle(Stationery):
    def draw(self):
        # title = 'Маркером'
        return f'Отрисовка {self.title}.'


my_start = Stationery()
print(my_start.draw())
my_pen = Pen('Ручкой')
print(my_pen.draw())
my_pencil = Pencil('Карандашом')
print(my_pencil.draw())
my_handle = Handle('Маркером')
print(my_handle.draw())
