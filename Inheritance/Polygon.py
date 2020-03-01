class Polygon:
    width = None
    height = None

    def set_value(self, width, height):
        self.width = width
        self.height = height


class Rectangle(Polygon):
    def area(self):
        return self.width * self.height

class Triangle(Polygon):
    def area(self):
        return self.width * self.height / 2

rect = Rectangle()
tri = Triangle()

rect.set_value(10, 10)
tri.set_value(10, 10)

print("khan:" ,+ rect.area())
print(tri.area())