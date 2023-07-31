# How to Print Multiple Arguments in Python?
def print_multiple_args(*args):
    for arg in args:
        print(arg, end=" ")

name = "John"
age = 30
occ= "Engineer"

print_multiple_args("Name:", name, "Age:", age, "Occupation:", occ)


