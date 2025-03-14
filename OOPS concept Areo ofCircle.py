class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.143 * self.radius * self.radius
circle1=Circle(10)
print(circle1.area())