# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name 
        self.max_speed = max_speed
        self.mileage = mileage 

    def seating_capacity(self, capacity): 
        return f"The capacity of the {self.name} is {capacity} passengers "


class Bus(Vehicle):
    # assign default value to capacity
    # class super to call the parent function 
    def seating_capacity(self, capacity = 50):
        return super().seating_capacity(capacity = 50)
        

schoolBus = Bus("SB", 240, 24)
print(schoolBus.seating_capacity())