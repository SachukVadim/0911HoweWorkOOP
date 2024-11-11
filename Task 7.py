class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors, fuel_type):
        super().__init__(make, model, year)
        self.num_doors = num_doors
        self.fuel_type = fuel_type

    def display_info(self):
        super().display_info()
        print(f"Тип: Автомобіль, Дверей: {self.num_doors}, Тип палива: {self.fuel_type}")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_capacity):
        super().__init__(make, model, year)
        self.engine_capacity = engine_capacity

    def display_info(self):
        super().display_info()
        print(f"Тип: Мотоцикл, Об'єм двигуна: {self.engine_capacity} куб. см")


class Truck(Vehicle):
    def __init__(self, make, model, year, max_load):
        super().__init__(make, model, year)
        self.max_load = max_load

    def display_info(self):
        super().display_info()
        print(f"Тип: Вантажівка, Максимальне навантаження: {self.max_load} кг")


car = Car("Toyota", "Camry", 2020, 4, "Бензин")
motorcycle = Motorcycle("Honda", "CBR600RR", 2018, 600)
truck = Truck("Volvo", "FH16", 2019, 20000)

car.display_info()
print()
motorcycle.display_info()
print()
truck.display_info()
