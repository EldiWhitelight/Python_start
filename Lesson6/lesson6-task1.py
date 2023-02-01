#1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный)
# — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.

import time


class TrafficLight:
     __color = 'red'

     def running(self):
         print(self.__color)
         cycle = ['red', 'yellow', 'green']
         i = 0
         while True:
             if self.__color == 'red':
                 time.sleep(7)
                 self.__color = 'yellow'
             elif self.__color == 'yellow':
                 time.sleep(2)
                 self.__color = 'green'
             elif self.__color == 'green':
                 time.sleep(7)
                 self.__color = 'red'
             i += 1  # счетчик +1
             if i >= len(cycle):  # счетчик достиг или превысил количество элементов в цикле и обнуляется
                 i = 0
             if self.__color == cycle[i]:  # проверка правильности
                 print(self.__color)
             else:
                 break

tl = TrafficLight()
tl.running()