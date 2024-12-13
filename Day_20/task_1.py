# Create a class Person with instance attributes name and age. Create a method get_details in this class to print name and age.

class Person:

    def __init__(self, name, age):  # Constructor to initialize instance attributes
        self.name = name # instance attribute
        self.age = age # instance attribute

    def get_details(self): # method 
        print(f"Name is {self.name} and age is {self.age}")

p = Person("Balen", 36) # Creating an instance of the Person class
print(p.name) # Balen
print(p.age) # 36

p.get_details()