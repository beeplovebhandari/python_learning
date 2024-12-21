# We can handle the files using Python
# In file handling we study how to open a file, read a file, write a file and close a file 

# r ==> Read MOde
# w ==> Write Mode
# r+ ==> Read and Write Mode
# w+ ==> Write and Read Mode

filename = "message.txt"

# Write Mode

fp = open(filename, "w")
fp.write("Hello World")
fp.close()


# Read Mode

fp = open(filename, "r")
data = fp.read()
fp.close()
print(data)

# Read and Write Mode

fp = open(filename, "r+")
data = fp.read()
fp.write("I'm learning python")
fp.close()

# Write and Read Mode

fp = open(filename, "w+")
fp.write("Python is a high level language ")
daa = fp.read()
fp.close
print(data)