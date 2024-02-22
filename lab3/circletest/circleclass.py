import math
class Circle:
    def __init__(self, radius = 0):
        radius = float(input('Please enter a radius. '))
        self.radius = radius

    def calculate_diameter(self):
        diameter = 2 * self.radius
        return diameter

    def calculate_circumference(self):
        circum = 2 * math.pi * self.radius
        return circum
    def get_area(self):
        area = math.pi * (self.radius ** 2)
        return area
    def grow(self):
        self.radius *= 2

    def get_radius(self):
        return self.radius