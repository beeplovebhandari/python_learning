# Concatenation (+)

a = (1, 2, 3)
b = (5, 6, 7)
result = a + b
print(result) # (1, 2, 3, 4, 5, 6)


# Repetition / broadcast (*)
a = (1, 2)
result = a * 3
print(result) # (1, 2, 1, 2, 1, 2)


# Membershi Opertaion
 
print(2 in (1, 2, 3)) # True
print(2 not in (1, 2, 3)) # False


# Iteration
vowels  = ("a", "e", "i", "o", "u")
for each in vowels:
    print(each) #a e i o u 

data  =[i**2 for i in range (10)] # List comprehension
print(data)
data  =(i**2 for i in range (10)) # Generator expression
print(data)
