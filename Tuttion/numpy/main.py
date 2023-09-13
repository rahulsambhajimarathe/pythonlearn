from numpy import *

# array
# a = array([1, 2, 3, 4, 5 , 6, 7, 8, 9])
# for x in a:
#     print(x)
    
# b = 0
# while b > len(a):
#     print(a[b])
#     b+=1



# linespace
# a = linspace(1, 10, 10)
# for x in a:
#     print(x)

# b = 0
# while b < len(a):
#     print(a[b])
#     b+=1


# logspace
# a = logspace(1, 10, 10)
# print(a)
# for x in a:
#     print(x)
    
# b = 0
# while b < len(a):
#     print(a[b])
#     b+=1


# a = arange(10)
# for b in a:
#     print(b)
# b = 0
# while b < len(a):
#     print(a[b])
#     b+=1

# a = zeros(10)
# for x in a:
#     print(x)

# b = 0
# while b < len(a):
#     print(a[b])
#     b+=1


# ones
# a = ones(10)
# for x in a:
#     print(x)

# b = 0
# while b < len(a):
#     print(a[b])
#     b+=1

# any
# def my_any(a, b):
#     main = a == b
#     for x in main:
#         if x == True:
#             return True
#             break

#     return True

# a = array([1, 2, 3, 4])
# b = array([1, 2, 3, 5])
# print(my_any(a, b))

# all
# def my_all(a, b):
#     main = a == b
#     for x in main:
#         if x == False:
#             return False
#             break
#     return True

# a = array([3, 1, 5, 87])
# b = array([1, 2, 3, 4])
# print(my_all(a, b))

# a = array([1, 2, 3, 5, 87, 1, 6, 7, 9, 23, 643, 423])
# b = reshape(a, (2, 6))
# for i in b:
#     print(i)
#     for r in i:
#         print(r)


# a = array([1, 2, 3, 5, 87, 1, 6, 7, 9, 23, 643, 423])
# b = reshape(a, (2, 6))
# c = 0
# while c < len(b):
#     d = 0
#     while d < len(b[c]):
#         print(b[c][d])
#         d += 1
#     c += 1

# a = array([1, 2, 3, 5, 87, 1, 6, 7, 9, 23, 643, 423])
# b = reshape(a, (3, 4))
# for i in b:
#     for r in i:
#         print(r)


a = array([1, 2, 3, 5, 87, 1, 6, 7, 9, 23, 643, 423])
b = reshape(a, (3, 4))
c = 0
while c < len(b):
    d = 0
    while d < len(b[c]):
        print(b[c][d])
        d += 1
    c += 1