# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

from random import randint

# Создаем файл
n = int(input("Укажите количество чисел: "))
numbers = [str(randint(0, 50)) for i in range(n)]
with open('lesson5-task5.txt', 'w', encoding='utf-8') as txt:
     txt.write(' '.join(numbers))

# Считаем сумму
with open('lesson5-task5.txt', 'r', encoding='utf-8') as txt:
     content = list(map(int, txt.read().strip().split()))
     print(f'Сумма равна {sum(content)}')