##plaindrom
#
#a = "656"
#b = "-"
#for i in range("6541"):
#    print(i)
#

#PS C:\Users\Acer> & C:/Python311/python.exe c:/Users/Acer/OneDrive/Desktop/num.py
#Traceback (most recent call last):
#  File "c:\Users\Acer\OneDrive\Desktopnum.py", line 3, in <module>
#    for i in range("6541"):
#             ^^^^^^^^^^^^^
#TypeError: 'str' object cannot be interpreted as an integer
#
"""
string = "8746"
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string


if string == reversed_string:
    print("Your number is palindrome:", string, "==", reversed_string)
else:
    print("Your number is not palindrome", string, "==", reversed_string)"""
    
    
    
#/1 to 10
"""a = 0
while a <=10:
    print("Your number is:", a)
    a += 1"""
    
    
#10 to 1
"""a = 10
while a >=1:
    print("Your number is:", a)
    a -= 1"""


#armstrong 
"""string = "8746"
b =0
for char in string:
    a = count(int(char))
    
    b = a //1"""
 
   
    
num = 371

sum = 0

temp = num

while temp>0:
    digitis = temp % 10
    sum += digitis **3
    temp //= 10
    
if num == sum:
    print(num, "==", sum, "you have a armstrong digits")
else:
    print(num, "==", sum, "you have not a armstrong digits")





#print(356%356)