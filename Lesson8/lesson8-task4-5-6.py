# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).

class NoEmptyCellsError(Exception): # нет свободных ячеек

    def __init__(self, txt):
        self.txt = txt


class WeightError(Exception): # большой вес на ячейку

    def __init__(self, txt):
        self.txt = txt


class EnoughQuantityError(Exception): # нет техники

    def __init__(self, txt):
        self.txt = txt


class Storage:

    def __init__(self, cells, weight_per_cell):
        self.cells = cells  # всего ячеек
        self.empty_cells = cells  # количество свободных ячеек
        self.weight_per_cell = weight_per_cell  # максимальная нагрузка на одну ячейку
        self.on_storage = {}  # словарь техники модель: количество

    @property
    def get_empty_cells(self):
        return f'Осталось {self.empty_cells} свободных ячеек'

    def to_storage(self, office_equipment, quantity=1):
        try:  # исключение, когда количество не число
            quantity = int(quantity)
        except ValueError:
            print("Количество техники должно быть числом")
        else:
            try:  # исключение, недостаточно свободных ячеек
                if self.empty_cells < office_equipment.volume * quantity:
                    raise NoEmptyCellsError("Недостаточно свободных ячеек")
            except NoEmptyCellsError as e:
                print(e)
            else:
                try:  # исключение, когда превышается максимальная нагрузка на ячейку
                    if office_equipment.weight / office_equipment.volume > self.weight_per_cell:
                        raise WeightError("Техника слишком тяжелая")
                except WeightError as e:
                    print(e)
                else:
                    # текущее количества данной техники на складе, при отсутствии создание пары модель: None
                    numbers = self.on_storage.setdefault(office_equipment.model)
                    if numbers:
                        self.on_storage[office_equipment.model] += quantity
                    else:
                        self.on_storage[office_equipment.model] = quantity
                    self.empty_cells -= office_equipment.volume * quantity  # ячейки заняты
                    print(f"Техника {office_equipment} в количестве {quantity} размещена на складе")
                    print(self.get_empty_cells)

    def from_storage(self, office_equipment, department, quantity=1):
        try:
            quantity = int(quantity)
        except ValueError:
            print("Количество должно быть числом")
        else:
            try:  # исключение при недостаточном количестве техники на складе
                if self.on_storage[office_equipment.model] < quantity:
                    raise EnoughQuantityError(f"Недостаточно техники {office_equipment.model} на складе")
            except EnoughQuantityError as e:
                print(e)
            else:
                self.on_storage[office_equipment.model] -= quantity
                self.empty_cells += quantity * office_equipment.volume  # увеличение кол-ва освободившихся ячеек
                print(f"Техника {office_equipment} в количестве {quantity} размещена в {department}")
                print(self.get_empty_cells)


class OfficeEquipment:
    def __init__(self, brand, model, price, weight, volume):
        self.brand = brand
        self.model = model
        self.price = price
        self.weight = weight
        self.volume = volume  # сколько ячеек занимает

    def __str__(self):
        return f'{self.brand} {self.model}'


class Printer(OfficeEquipment):
    def __init__(self, brand, model, price, weight, volume, type):
        super().__init__(brand, model, price, weight, volume)
        self.type = type


class Scanner(OfficeEquipment):
    def __init__(self, brand, model, price, weight, volume, resolution):
        super().__init__(brand, model, price, weight, volume)
        self.resolution = resolution


class Copier(OfficeEquipment):
    def __init__(self, brand, model, price, weight, volume, is_colour):
        super().__init__(brand, model, price, weight, volume)
        self.is_colour = is_colour


# проверяем
printer_1 = Printer('HP', "222", 3000, 15, 2, 'струйный')
scanner_1 = Scanner('HP', "333", 4000, 10, 1, 1200)
scanner_2 = Scanner('Epson', "444", 5000, 10, 2, 1200)
copier_1 = Copier('Epson', "555", 1000, 25, 3, True)
storage1 = Storage(30, 9.99)

print(storage1.get_empty_cells)
storage1.to_storage(printer_1)
storage1.to_storage(copier_1, 3)
storage1.to_storage(copier_1, 100)
storage1.to_storage(copier_1, 'один')
storage1.to_storage(scanner_1)
storage1.to_storage(scanner_2)
storage1.to_storage(scanner_2)

storage1.from_storage(copier_1, 'кадры')
storage1.from_storage(copier_1, 'бухгалтерия', 3)
storage1.from_storage(scanner_2, 'производство', 'два')