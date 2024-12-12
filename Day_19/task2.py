# wap to delete all the occurrences of specified charcater in a given string 

#method 1
char_to_remove = input("Enter a chracter you want to remove: ")
text = "All the occurrences of a specified character in a given string"
result = text.replace(char_to_remove, "")
print(result)


#method 2 using loop

char_to_remove = input("Enter a chracter you want to remove: ")
text = "All the occurrences of a specified character in a given string"
result = ""
for each in text:
    if each.lower() == char_to_remove.lower():
        continue
    result += each
print(result)