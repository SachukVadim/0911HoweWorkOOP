from datetime import date


class MyClass1:
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, surname, name, birthYear):
        return cls(surname, name, date.today().year - birthYear)

    @staticmethod
    def is_adult(age):
        return age >= 18

    def print_info(self):
        print(self.surname + " " + self.name + "'s age is: " + str(self.age))


class MyClass2(MyClass1):
    color = 'White'
    adults_count = 0

    def __init__(self, surname, name, age):
        super().__init__(surname, name, age)
        if self.is_adult(age):
            MyClass2.adults_count += 1

    @classmethod
    def count_adults(cls):
        return cls.adults_count


m_per1 = MyClass1('Ivanenko', 'Ivan', 19)
m_per1.print_info()

m_per2 = MyClass1.fromBirthYear('Dovzhenko', 'Bogdan', 2000)
m_per2.print_info()

m_per3 = MyClass2.fromBirthYear('Sydorchuk', 'Petro', 2010)
print(isinstance(m_per3, MyClass2))

m_per4 = MyClass2.fromBirthYear('Makuschenko', 'Dmytro', 2001)
print(isinstance(m_per4, MyClass1))

print(MyClass2.count_adults())  # Підрахуємо кількість повнолітніх

print(issubclass(MyClass1, MyClass2))
print(issubclass(MyClass2, MyClass1))
