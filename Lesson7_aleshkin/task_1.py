"""
Задание 1.

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init()__),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода __str()__ для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add()__ для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18
"""


class Matrix:
    def __init__(self, mydata):
        self.mydata = mydata

    #перегрузка метода для вывода matrix
    def __str__(self):
        rows = []
        for row in self.mydata:
            rows.append(' '.join(str(num) for num in row))
        return '\n'.join(rows)

    #перегрузка метода для сложения
    def __add__(self, newdata):
        result = []
        for i in range(len(self.mydata)):
            row = []
            for el in range(len(self.mydata[i])):
                row.append(self.mydata[i][el] + newdata.mydata[i][el])
            result.append(row)
        return Matrix(result)

matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(f'Матрица 1:\n{matrix1}\nМатрица 2:\n{matrix2}')
print(f'Сумма матриц:\n{matrix1 + matrix2}')

