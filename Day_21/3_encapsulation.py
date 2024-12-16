# Encapsulation is the process of data hiding in OOP approach of programming.
# Using this feature we make our attributes private, public or/and protected

# Public Attributes
# These attributes are accesible from both inside the class and outside the class

class Vehicle:
    engine_type = "Petrol" #Public

    def description(self):
        return f"The vehicle has{self.engine_type} engine"
    
v = Vehicle()
print(v.engine_type) #Petrol



# Protected Attributes
# This attributes should accessible form the same class or the child class only

class Vehicle:
    _color = "blue" # Protected member because of the sinhle underscore in the beginning of the variable 

    def color_desc(self):
        print(f"The color of the vehicle is {self._color}")

class Bike(Vehicle):
    def color_desc(self):
        return (f"The color of the bike is {self._color}")
    
b = Bike()
print(b._color) #blue. ;; Python is flexible so it also allows the protected members to be accessible from outside the class . But, it is not recommended to do so.



# Private Attributes

class Vehicle:
    __color = "red" # Private member because of the double underscore in the beginning of the variable 

    def color_desc(self):
        return f"The color of the variable is {self.__color}"
    
v = Vehicle()
# print(v.__color) # Attribute Error
print(v.color_desc()) # Attribute Error

