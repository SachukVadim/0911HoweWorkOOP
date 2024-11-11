class GraphicObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(f"Графічний об'єкт створений на позиції ({self.x}, {self.y}).")


class Rectangle(GraphicObject):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height
        print(f"Прямокутник створений на позиції ({self.x}, {self.y}) з розмірами {self.width}x{self.height}.")


class Clickable:
    def click(self):
        print("Об'єкт натиснуто.")


class Button(Rectangle, Clickable):
    def __init__(self, x, y, width, height, label="Кнопка"):
        super().__init__(x, y, width, height)
        self.label = label

    def click(self):
        print(f"Кнопка '{self.label}' натиснута.")


button = Button(10, 20, 100, 50, "OK")
rectangle = Rectangle(30, 40, 200, 100)

button.click()
