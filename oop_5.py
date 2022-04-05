# Create a Bus child class that inherits from the Vehicle class. 
# The default fare charge of any vehicle is seating capacity * 100. 
# If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. 
# So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
class vehicle : 
    def __init__(self,name,mileage,capacity) : 
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self) :
        return self.capacity*100

class Bus(vehicle) :
    def fare(self):
        amount = super().fare()
        amount += amount * 10/100
        return amount

school_bus = Bus("SB",50,50)
print(type(school_bus))
print(f"Is school bus an instance of vehicle ? : {isinstance(school_bus,vehicle)}")
print("Full fare is : ",school_bus.fare())

