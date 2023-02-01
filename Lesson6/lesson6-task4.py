# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
# turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Начало движения')

    def stop(self):
        print('Остановка')
        self.speed = 0  # 0 скорость при остановке

    def turn(self, direction):
        print(f'Поворот {direction}')

    def show_speed(self):
        print(f'Скорость движения {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Скорость более 60 км/ч, тормози")


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Скорость более 40 км/ч, тормози!")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


car1 = TownCar(100, 'синий', 'Mini')
car2 = TownCar(62, 'красный', 'Smart')
car3 = WorkCar(41, 'черный', 'Man')
car4 = PoliceCar(110, 'белый', 'Mazda')

# доступ к атрибутам
print(car1.speed, car2.color, car2.name, car4.is_police, car3.is_police)

# Проверяем
car1.go()
car2.stop()
car3.turn('Направо')
car1.show_speed()
car2.show_speed()
car3.show_speed()
car4.show_speed()