"""
Задание 1.

Реализовать класс «Дата», на уровне класса определить атрибут day_month_year,
присвоить ему значение

В рамках класса реализовать два метода.

Первый, с декоратором @classmethod, должен извлекать число, месяц,
год, преобразовывать их тип к типу «Число» и делать атрибутами класса.

Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""
"""
Реализовать класс «Дата»,
функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
(например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Data:
    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    @classmethod
    def extract_date(cls, day_month_year):
        day, month, year = map(int, day_month_year.split('-'))
        return day, month, year

    @staticmethod
    def valid_date(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2023 >= year >= 0:
                    return f'Всё верно.'
                else:
                    return f'Неверный год.'
            else:
                return f'Неверный месяц.'
        else:
            return f'Неверный день.'

    def __str__(self):
        return f'Сегодня: {Data.extract_date(self.day_month_year)}'


day_month_year = "24 - 08 - 2023"
today = Data(day_month_year)

print(today)
print(Data.extract_date(day_month_year))
print(Data.valid_date(32, 5, 2077))
