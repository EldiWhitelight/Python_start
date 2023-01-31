# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные
# о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

import json

# Создаем словарь
with open('lesson5-task7.txt', 'r', encoding='utf-8') as txt:
     dict = {line.strip().split()[0]: int(line.strip().split()[2]) - int(line.strip().split()[3]) for
                      line in txt}

# Средняя прибыль
sum_profit = 0  # дефолтное значение
profit_firms = 0  # дефолтное значение для прибыльных фирм
for value in dict.values():
     if value >= 0:
         sum_profit += value
         profit_firms += 1
average_profit = sum_profit / profit_firms

 # создание списка из 2х словарей
list_of_firms = [dict, {"average_profit": average_profit}]

with open('lesson5-task7-result.json', 'w') as txt:
     json.dump(list_of_firms, txt, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))