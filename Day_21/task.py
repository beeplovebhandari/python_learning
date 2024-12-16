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

# Create another class Employee with attributes salary and designation and inheritsthe Person Class.
# Create a method get_details in this class to print name , age, salary and designation of the Employee.

class Employee(Person):
    def __init__(self, name, age, salary, designation):
        super().__init__(name, age)  # Initialize attributes from the parent class
        self.salary = salary         # Instance attribute for salary
        self.designation = designation  # Instance attribute for designation

    def get_details(self):  # Overriding the get_details method
        print(f"The Employee Mr.{self.name}, age {self.age}, earns {self.salary} as a {self.designation}.")


# Creating an instance of the Person class
p = Person("Balen", 36)
print(p.name)  # Output: Balen
print(p.age)   # Output: 36
p.get_details()  # Output: Name is Balen and age is 36

# Creating an instance of the Employee class
e = Employee("Ram", 30, 35000, "Python Developer")
print(e.name)  # Output: Ram
print(e.age)   # Output: 30
e.get_details()  # Output: The Employee Mr.Ram, age 30, earns 35000 as a Python Developer.
