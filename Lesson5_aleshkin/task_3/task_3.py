"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

#.....перевод.....
with open("numbers.txt", 'r', encoding='utf-8') as f_obj:
    for el_line in f_obj:
        words = el_line.split()
        """
        if words == 'One':
            words == 'Один'
        elif words == 'Two':
            words == 'Два'
        elif words == 'Three':
            words == 'Три'
        elif words == 'Four':
            words == 'Четыре'
        """
        print(el_line)