# WAP to create a function to do initial letter capital
# one = "dsafhul"
# print(one.capitalize())


# string = "hello ram"

# if string:
#     capitl = string[0].upper() + string[1:]
#     print(capitl)
# else:
#     print(string)



# WAP to create a function to capital all the letter

# def letters(string):
#     return string.upper()

# # Example usage
# text = "rahul marathe"
# up = letters(text)
# print(up)


# check the given string letters (all letters) is capital or small

# def givee(string):
#     if string.isupper():
#         return "uppercase"
#     elif string.islower():
#         return "lowercase"
#     else:
#         return "mix"

# # Example usage
# text1 = "dsaf dsfdA dsafhjk "

# print(givee(text1))


# remove all the spaces from left of string
# text = "    Hello World"
# print(text.lstrip())


# remove all the spaces from right of string

# text = "    Hello World     "
# print(text.rstrip())



# remove all the spaces from left and right of string
# text = "    Hello World     "
# print(text.strip())


# add user given string to your variable string, at the left side of string.
# text = "World"
# user= input("Enter a string: ")

# modi = user + text
# print(modi)




# WAP to check a specific word is exists or not
#     "hello everyone how are you?"
#     - find "how"
#         if this is exists give true else false



# sen = input("Enter a sentence: ")
# word = input("Enter the target word: ")

# if word in sen:
#     print("True")
# else:
#     print("False")


# write a program in Python to remove an empty character from a list sequence.
#     Given n = [“name”,”age”,””,”hello”]
#     Output:  [‘name’, ‘age’, ‘hello’]

# n = ["name", "age", "", "hello"]
# res = []

# for ele in n:
#     if ele != "":
#         res.append(ele)

# print(res)


# Python program to convert all the starting letter of a word in upper case format or in the title format.
#     Given n = “hello this is pythonlobby”
#     Output: Hello This Is Pythonlobby

n = "hello this is pythonlobby"
b =""
for x in n:
    b = x.capitalize()
    
print(b)