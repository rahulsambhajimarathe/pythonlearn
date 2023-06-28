value1 = int(input("Enter a first value"))
oprator =input("Enter a + - * / to calulate next value")
value2 = int(input("Enter a second value"))

if oprator == "+":
    cal = value1+value2
    print("sum of two value", value1+value2)
elif oprator == "-":
    cal = value1-value2
    print("minus of two value", value1-value2)
elif oprator == "*":
    cal = value1*value2
    print("multiply of two value", value1*value2)
elif oprator == "/":
    cal = value1/value2
    print("devid of two value", value1*value2)
else:
    cal = value1%value2
    print("modulas of two value", value1%value2)
print("calulation is done", value1, oprator, value2, "=", cal)