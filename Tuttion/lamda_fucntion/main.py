# plus
# def sum(a):
#     def sum1(b):
#         print(a + b)

#     return sum1

# x = sum(40)
# x(50)


# minus
# def mul(a):
#     def mul1(b):
#         print(a * b)

#     return mul1

# x = mul(40)
# x(50)

# devide
# def dev(a):
#     def dev1(b):
#         print(a / b)

#     return dev1

# x = dev(40)
# x(50)



# minus
def min(a):
    def min1(b):
        print(a - b)

    return min1

x = min(50)
x(50)



# lamda

# sum
def sum(a):
    return lambda y: a+y

x = sum(100)
y = x(10)
print(y)



# minus

def minus(a):
    return lambda y: a-y

x = minus(100)
y = x(10)
print(y)



# devide


def dev(a):
    return lambda y: a/y

x = dev(100)
y = x(10)
print(y)



# multiply

def mul(a):
    return lambda y: a*y

x = mul(100)
y = x(10)
print(y)