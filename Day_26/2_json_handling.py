# JSON stands for Javascript Object Notation
# It is one of the file format to transfer data around the web or system 
# Its is a very famous way of file transfer in the REST APIs
# Python has a built-in support for json handling

# Rules in a json file
# 1. Keys and values must be enclosed in doub le quotes
# 2. Information can be enclosed in an array
# 3. Double quotes are not required for the number datatype
# 4. Extension of the JSON file is .json
#for example:
student = {"name" :" Jon", "address" : "KTM" } # This can be valid JSON
student = {'name' :'Jon', 'address' : 'KTM' } # Invalid JSON. JSON must have double qotes

students = [
    {"name" :" Jon", "address" : "KTM", "phone": 9898778979},
    {"name" :" Ram", "address" : "BKT", "phone": 98989989},
    {"name" :" Shyam", "address" : "PKR", "phone": 9898999889},
]
# Valid JSON

import json

filename = "students.json"
with open(filename, "w+") as fp:
    data = json.dumps(students, indent=2)
    fp.write(data)
    fp.seek(0)
    data = fp.read()
    data =json.loads(data)

name = data[0]["name"]
print(name)



