# Inheritance is the transfer of proporties and methods to the child class from the parent class
# Types of inheritance in pyhton;
# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multilevel Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance


class Vehicle: # Parent Class
    engine_type = "Petrol Engine"

class Bike(Vehicle):
    wheels = "two"

class  Car(Vehicle):
    wheels = "four"

car = Car()
print(car.engine_type) #petrol_engine
print(car.wheels) #four

class Cycle(Bike): #child ko ni further child
    engine_type = None





# Single Inheritance

class A:
    pass

class B(A): #This is single inheritance
    pass




# Multiple Inheritance

class A:
    pass

class B:
    pass


class C(A, B): # This is multiple inheritance
    pass



# Multilevel Inheritance

class A:
    pass

class B(A):  #b vitra a paryo ani muntira c vitra b paryo uo chai multilevel ho, dekhda single inheritance jasto dekhinxa
    pass
class C(B):
    pass



# Hierarchical Inheritance

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(A):
    pass


# mro ==> mro stands for method resolution order. It is the order in which attributes in inheritance is searched

class A:
    pass

class B(A):
    pass

class C(A):
    pass
class D(B, C):
    pass

class E(D):
    pass

e = E()
print(E.mro())