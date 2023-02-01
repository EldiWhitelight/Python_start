# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное
# сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки для ручки - {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки для карандаша - {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки для маркера - {self.title}')


# проверка методов
pen1 = Pen("Перьевая ручка")
pen1.draw()

pen1 = Pen("Гелиевая ручка")
pen1.draw()

pen2 = Pen("Простая ручка")
pen2.draw()

pencil1 = Pencil('Простой карандаш')
pencil1.draw()

pencil1 = Pencil('Механический карандаш')
pencil1.draw()

handle1 = Handle('Обычный маркер')
handle1.draw()

handle1 = Handle('Спиртовой маркер')
handle1.draw()