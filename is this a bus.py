class Vehicle:
    def __init__(self, name, maximum_speed, mileage):
        self.name = name
        self.maximum_speed = maximum_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", "100 mile per hour", "80 meter")
print("Name: {}\nMax Speed: {}\nMileage: {}".format(School_bus.name, School_bus.maximum_speed, School_bus.mileage))