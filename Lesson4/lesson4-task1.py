#Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для конкретных
# значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, time, rate, bonus = argv

print("script_name: ", script_name)
print("time: ", time)
print("rate: ", rate)
print("bonus: ", bonus)
print("salary: ", int(time)*int(rate)+int(bonus))