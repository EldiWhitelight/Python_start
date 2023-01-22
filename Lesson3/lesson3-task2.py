# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры
# как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.

def user_info(name=None, surname=None, year=None, email=None, phone=None, city=None,):
    print(f'Имя: {name}, Фамилия: {surname}, Год рождения: {year}, email: {email}, Телефон: {phone}, '
          f'Город: {city}')


user_name = input("Введите имя: ")
user_surname = input("Введите фамилию: ")
user_year = int(input("Введите год рождения: "))
user_email = input("Введите электронную почту: ")
user_phone = input("Введите номер телефона: ")
user_city = input("Введите город проживания: ")
user_info(name=user_name, year=user_year, surname=user_surname, email=user_email, phone=user_phone, city=user_city)