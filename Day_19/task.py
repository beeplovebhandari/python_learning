# Create a decorator to change all the characters of the input function to upper case

def to_upper_case(func):
    def inner_func(info):
        return func(info).upper()
    return inner_func

@to_upper_case
def message(info):
    return info 

result = message("Hello I'm learning Python")
print(result)


# First 20 multiple of 3

for i in range (1, 21):
    print(3*i)

 

n = 0
even_number_count = 0
while even_number_count != 50:
    if n % 2 == 0:
        print(n)
        even_number_count += 1
    n += 1