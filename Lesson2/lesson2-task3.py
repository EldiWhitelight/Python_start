# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и dict.


month = 0

# Запрашиваем у пользователя порядковый номер месяца. Если он указал несуществующий номер, выводим текст
while month not in range(1, 13):
    month = int(input("Укажите порядковый номер месяца: "))
    if month not in range(1, 13):
        print("Такого месяца не существует")

# Через list
seasons = ["зима", "весна", "лето", "осень"]
winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
# Остальное будет осенью

if month in winter:
    print(seasons[0])
elif month in spring:
    print(seasons[1])
elif month in summer:
    print(seasons[2])
else:
    print(seasons[3])

# Через dict
seasons_dict = {'зима': [1, 2, 12], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
for season, months in seasons_dict.items():
    if month in months:
        print(season)