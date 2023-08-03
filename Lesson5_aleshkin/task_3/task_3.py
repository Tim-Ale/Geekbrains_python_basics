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

numbers = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('numbers.txt', 'r', encoding='utf-8') as origfile:
    my_lines = origfile.readlines()

new_lines = []
for line in my_lines:
    word, file_number = line.strip().split(' — ')
    rus_number = numbers[word]
    # [word] -> [rus_number] + ' - ' + [file_number]
    new_line = f'{rus_number} — {file_number}\n'
    new_lines.append(new_line)

with open('new_numbers.txt', 'w', encoding='utf-8') as file:
    file.writelines(new_lines)
