class Math:
    chapters = ["Linear Alzebra", "Calculas"]

class Chemistry:
    chapters = ["Acid, Salt, Base"]

class Physics(Math, Chemistry):
    pass

p = Physics()
print(p.chapters) #['Linear Alzebra', 'Calculas']