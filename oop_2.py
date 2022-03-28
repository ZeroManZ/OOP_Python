# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class vehicle : 
    def __init__(self,name,max_speed,mileage) :
        self.name = name 
        self.max_speed = max_speed
        self.mileage = mileage

class Bus (vehicle) : 
    pass

School_Bus = Bus("SB",240,18)
print(School_Bus.name,School_Bus.max_speed,School_Bus.mileage)