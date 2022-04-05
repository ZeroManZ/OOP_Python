# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle : 
    def __init__(self, name, max_speed, mileage) :
        self.name = name 
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle) : 
    pass

schoolBus = Bus("SB",240,18)
print(schoolBus.name, schoolBus.max_speed, schoolBus.mileage)