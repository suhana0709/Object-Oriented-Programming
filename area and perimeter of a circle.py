class Circle:
    def __init__(self, radius):
        self.radius= radius

       #area
    def area(self):
        area = 22/7 * self.radius **2
        print("Area: ",area)

        #perimeter
    def perimeter(self):
        perimeter = 2 * 22/7 * self.radius
        print("Perimeter: ",perimeter)

a = Circle(7)
a.area()
a.perimeter()