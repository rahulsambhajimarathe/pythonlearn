"""import array

marks = array.array("i", [10, 50, 64, 73, 64])
i = 0

while i < len(marks):
    print(marks[i])
    i += 1
"""



"""from array import *

marks = array("i", [53, 64, 64, 354, 45])

for x in marks:
    print(x)"""
    
    



    
    
"""from array import *

marks = array("i", [53, 64, 64, 354, 45])

i = 0
while i < len(marks):
    print(marks[i])
    i += 1"""







"""from array import *

my_array = array("i", [])

print(my_array)"""




"""
from array import *

my_array = array("i", [])

value = int(input("Enter a value: "))

my_array.append(value)

print(my_array)
"""


"""from array import *

marks = array("i", [])

while True:
    value = int(input("Enter a value (Enter -1 to stop): "))
    if value == -1:
        break
    marks.append(value)

print(marks)
"""



from array import *

marks = array("i", [10, 45, 34, 63, 74, 10, 73, 65, 10 , 10, 10])
value = 10

# Removing all occurrences of the given value
while value in marks:
    marks.remove(value)

print(marks)
