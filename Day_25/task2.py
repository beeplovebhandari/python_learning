"""
Create a dictionary student with keys id, name, age, department. Take a input from the user , which info
(is, name, age or department) he wants to acess and print the result. Handle the possible exceptions.
"""

student = {"id":12, "name": "Ram", "age": 19, "department":"IT"}
try:
    key = input("Enter the key you want to access ")
    data = student[key]
    print(f"The {key} of the student is {data}")
except KeyError:
    print("Please enter a valid key")
