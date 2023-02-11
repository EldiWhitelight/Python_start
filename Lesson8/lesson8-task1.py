# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Date:
    def __init__(self, date):
        self.date = date.split('-')

    @classmethod
    def extract(cls, date):
        date = date.split('-')
        day = int(date[0])
        month = int(date[1])
        year = int(date[2])
        return day, month, year

    @staticmethod
    def check_date(date):
        day, month, year = Date.extract(date)
        good_date = True

        def bad_date():
            nonlocal good_date
            good_date = False # Присваиваем false если дата не верна


        if month < 1 or month > 12:  # проверка месяца от 1 до 12
            print(f"Число месяца должно быть от 1 до 12, введено {month}")
            bad_date()
        if month == 2 and (day > 29 or day < 1):  # проверка дней февраля, без учета високосных лет
            print(f"Для месяца {month} указано не верное количество дней {day}")
            bad_date()
        elif month in (1, 3, 5, 7, 8, 10, 12) and (day > 31 or day < 1):  # проверка даты в месяцах с 31 днем
            print(f"Для месяца {month} указано не верное количество дней {day}")
            bad_date()
        elif month in (4, 6, 9, 11) and (day > 30 or day < 1):  # проверка даты в месяцах с 30 днями
            print(f"Для месяца {month} указано не верное количество дней {day}")
            bad_date()
        if year > 2050 or year < 0:  # задаем диапазон и проверяем даты
            print(f"Значение года должно быть от 0 до 2050, введено {year}")
            bad_date()
        if good_date:
            print("Дата верна")


# Проверяем
Date.check_date("30-02-2000")
print()
Date.check_date("30-15-2001")
print()
Date.check_date("31-04-2052")
print()
Date.check_date("26-04-1993")
print()
Date.check_date("29-02-1900")