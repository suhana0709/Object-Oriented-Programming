#creating a class
class Vehicle:
    
    #create _init_ method
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

#object creation
vehicle = Vehicle(240, 18)

#access the variables inside the init method
print("Max Speed: ",vehicle.max_speed)
print("Mileage: ",vehicle.mileage)