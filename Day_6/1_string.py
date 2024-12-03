###### Accesing chracteres in String  #####
# We access chracters from string using indexing. Indexing in string is similar to that list
# Forward indexing starts from 0 and reverse indexing starts from -1


message = "Hello World"
print(message[0]) # H
print(message[3]) # L
print(message[5]) # <space>


print(message[-1]) #d
print(message[-3]) #r


# IF WE TRY TO ACCESS INDEX NOT PRESENT IN THE STRING THEN IT RAISES ERROR.

# print(message[15]) # It raises index error
# print(message[-13]) # It raises index error


########### String Slicing #############

#String slicing is also similar to list slicing

message = "Hello World"
print(message[0:3]) #Hel
print(message[:3]) #Hel
print(message[4:]) # o World
print(message[2:5])  #llo
print(message[3:-2])  #lo Wor
print(message[5:2])  #" "

print(message[:-2]) #Hello Wor
print(message[:0-2]) #Hello Wor
print(message[-4:]) # orld


print(message[-6: -2]) #" Wor"
print(message[-2: -6]) #" "



# Updating and deleting String Item

m = "Hello World"
# m[2] = "L" ##It raises error because string is immutable and item assigning isn't possible
# print(m) 

# del m[6] # this is aso not possible
# But we can entirely delete the string object

del m # It deletes the string onject m


# Iterating string using for loop

message = "Hello World"
for i in message:
    print(i) # H,e,l,l,o , W,o,r,l,d

for i in message[2:7]:
    print(i) # l,l,o ,W

