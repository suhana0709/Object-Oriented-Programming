#parent class
class Vehicle:
    def __init__(self, fare):
        self.fare = fare

#child class
class Bus(Vehicle):
    def __init__(self, fare, passenger):
        self.passenger = passenger
        Vehicle.__init__(self, fare)

    def total(self):
        print("Total bus fare: ",self.fare*self.passenger )

#object
a = Bus(50, 4)
a.total()
