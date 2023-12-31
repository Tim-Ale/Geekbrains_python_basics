"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

import time

class TrafficLight:
    def __init__(self):
        self.__color = ["красный", "желтый", "зеленый"]
        
    def running(self):
        for i in range(work_time):
            if i == 0:
                print(f"Светофор: {self.__color[0]}")
                time.sleep(7)
            elif i == 1:
                print(f"Светофор: {self.__color[1]}")
                time.sleep(2)
            elif i == 2:
                print(f"Светофор: {self.__color[2]}")
                time.sleep(4)

work_time = 3

my_traffic_light = TrafficLight()
my_traffic_light.running()
