from array import *

my_array = array("i", [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

for r in range(my_array[::]):
    for c in range(r):
        print(c)

# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#this is the odd even '
"""
from array import *

# Creating an array
my_array = array("i", [1, 2, 3, 4, 5, 6, 7, 8, 8945, 65, 4])

even_array = array("i", [])
odd_array = array("i", [])
for num in my_array:
    if num % 2 == 0:
        even_array.append(num)
    else:
        odd_array.append(num)


print("Original Array:", my_array)
print("Even Numbers Array:", even_array)
print("Odd Numbers Array:", odd_array)"""





