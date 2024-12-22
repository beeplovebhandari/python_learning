# Different modes in which files can be opened

# r ==> Read MOde
# w ==> Write Mode
# a ==> append Mode
# r+ ==> Read and Write Mode
# w+ ==> Write and Read Mode
# a+ ==> append and read Mode
# x  ==> Write exclusively Mode



filename = "message1.txt"
fp = open(filename, "w")
fp.write("Hello World")
fp.close()

fp = open(filename, "r")
data = fp.read()
print(data)
fp.close()

# fp = open(filename, "a")
# fp.write("\nI'm Learning Python")
# fp.close()


# file handling with context manager

with open(filename, "r") as fp:    # context manager
    data = fp.read()
print(data)


with open(filename, "r+") as fp:
    data = fp.read() # first read 
    fp.write("Python is a high level language") # and then read
print(data)

with open(filename, "w+") as fp:
    fp.write("I'm learning python") # first write
    data = fp.read()
print(data)

# exclusive mode doesn't create a file if the file already exists. It raises error in suh case

# with open(filename, "x") as fp:
#     fp.write("Hello World")

