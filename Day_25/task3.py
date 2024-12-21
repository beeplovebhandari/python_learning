# Create a function to check whether a input chracter is vowel or not .
# Handle the possible exceptions.

def is_vowel(char):
    if type(char) != str:
        return False
    if char.isnumeric():
        return False
    return char.lower() in ["a", "e", "i", "o", "u"]


result = is_vowel(2)
print(result)

result = is_vowel("A")
print(result)