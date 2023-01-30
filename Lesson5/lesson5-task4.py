# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные
# должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

numbers = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('lesson5-task4.txt', 'r', encoding='utf-8') as txt:
     with open('lesson5-task4_result.txt', 'w', encoding='utf-8') as result:
         for line in txt:
             content = line.split()
             result.write(' '.join([numbers[content[0]], content[1], content[2]])+'\n')