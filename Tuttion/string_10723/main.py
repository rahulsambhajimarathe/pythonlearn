
# one = "hello my name is rahul marathe"
# a = "king"
# b = ""
# if a in one:
#     b = True    
# else:
#     b = False
    
# print(b)

# x = ord("Z")
# print(x) 1



# code = "RAM" 
# for x in code:
#     j = ord(x) 
#     if j >= 65 and j <= 90:
#         c = True
#     else:
#         c = False
#         break
# print(c)


# code = "rAM" 
# c = ""
# for x in code:
    
#     j = ord(x)
#     # print(j)
    
#     if j >= 65 and j <= 90:
#         j += 32
#         c += chr(j)
#     elif j >= 91 and j <= 122:
#         j -= 32
#         c += chr(j)
# print(c)

user = int(input("enter how many spaces you want :"))
sentace = input("enter the sentance :")

c = " "
k = ""
pre = "currently das baj rahe hae abhi raat kae"
for x in range(user):
    k += c
sentace += k + pre
print(sentace)